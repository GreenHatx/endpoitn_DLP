import  sys,ctypes
import os
import db_handler as db
import helper
import winWatcher


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
path = helper.desktopFilePath
os.chdir(path)
db.mycursor.execute("DELETE FROM alerts")

if __name__ == "__main__":
    #db.connect_db()
    if helper.is_admin():
        w = winWatcher.Watcher(helper.desktopFilePath)
        w.run()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
