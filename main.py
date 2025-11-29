import os
import sys
import subprocess
import time
import signal
import platform
import webbrowser

# Configuration
BACKEND_PORT = 8000
FRONTEND_PORT = 5001
BACKEND_PID_FILE = "backend.pid"
FRONTEND_PID_FILE = "frontend.pid"
BACKEND_LOG = "backend.log"
FRONTEND_LOG = "frontend.log"

IS_WINDOWS = platform.system() == "Windows"

def get_venv_python():
    """Returns the path to the python executable in the local venv."""
    if IS_WINDOWS:
        return os.path.join("venv", "Scripts", "python.exe")
    else:
        return os.path.join("venv", "bin", "python")

def is_running(pid):
    """Checks if a process with the given PID is running."""
    try:
        # Signal 0 does nothing but error checking
        os.kill(pid, 0) 
        return True
    except OSError:
        return False

def start():
    print("Starting Smart Parking System (Portable)...")
    
    python_exe = get_venv_python()
    if not os.path.exists(python_exe):
        print(f"Error: Virtual environment not found at '{python_exe}'.")
        print("Please run the setup instructions in README.md first.")
        return

    # 1. Start Backend
    print(f"Launching Backend on port {BACKEND_PORT}...")
    with open(BACKEND_LOG, "w") as log:
        backend_proc = subprocess.Popen(
            [python_exe, "-m", "uvicorn", "backend.main:app", "--reload", "--port", str(BACKEND_PORT)],
            stdout=log,
            stderr=log
        )
    with open(BACKEND_PID_FILE, "w") as f:
        f.write(str(backend_proc.pid))

    # 2. Start Frontend
    print(f"Launching Frontend on port {FRONTEND_PORT}...")
    with open(FRONTEND_LOG, "w") as log:
        frontend_env = os.environ.copy()
        frontend_env["FASTAPI_BASE_URL"] = f"http://127.0.0.1:{BACKEND_PORT}"
        frontend_env["FLASK_RUN_PORT"] = str(FRONTEND_PORT)
        
        frontend_proc = subprocess.Popen(
            [python_exe, "frontend_flask/app.py"],
            stdout=log,
            stderr=log,
            env=frontend_env
        )
    with open(FRONTEND_PID_FILE, "w") as f:
        f.write(str(frontend_proc.pid))

    frontend_url = f"http://127.0.0.1:{FRONTEND_PORT}"
    print("\nServices started successfully!")
    print(f"Backend API: http://127.0.0.1:{BACKEND_PORT}")
    print(f"Frontend UI: {frontend_url}")
    print("\nLogs are being written to backend.log and frontend.log")
    print("Run 'python main.py stop' to shut down.")
    
    print("Opening browser...")
    time.sleep(2) # Give servers a moment to initialize
    webbrowser.open(frontend_url)

def stop():
    print("Stopping services...")
    for pid_file, name in [(BACKEND_PID_FILE, "Backend"), (FRONTEND_PID_FILE, "Frontend")]:
        if os.path.exists(pid_file):
            try:
                with open(pid_file, "r") as f:
                    pid = int(f.read().strip())
                
                if is_running(pid):
                    os.kill(pid, signal.SIGTERM)
                    print(f"Stopped {name} (PID {pid})")
                else:
                    print(f"{name} was not running.")
                
                os.remove(pid_file)
            except Exception as e:
                print(f"Error stopping {name}: {e}")
        else:
            print(f"No PID file found for {name}.")

def restart():
    stop()
    time.sleep(2)
    start()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py [start|stop|restart]")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "start":
        start()
    elif command == "stop":
        stop()
    elif command == "restart":
        restart()
    else:
        print(f"Unknown command: {command}")
        print("Usage: python main.py [start|stop|restart]")
