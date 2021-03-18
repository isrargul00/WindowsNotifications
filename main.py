from win10toast import ToastNotifier
import requests
notfy = ToastNotifier()

def main():
    notfy.show_toast('Python',"Python Deskstop Notifications System ", duration=10)

if __name__ == '__main__':
    main()
