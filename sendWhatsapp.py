import pyautogui
import time

# Get the current mouse position
position = pyautogui.position()

# Define the message to be typed
pesan = "visualisasi data dalam pembelajaran sangat berkontribusi baik dalam pembelajaran, terkhusus untuk diri saya sendiri, saya lebih mudah memahami materi yang divisualkan datanya daripada harus membaca tulisan yang banyak, karena salah satu metode belajar yang mudah dan menyenangkan adalah dengan metode divisualkan, maka tidak heran banyak anak-anak bayi yang diberikan pembelajaran pertama oleh orang tuanya dengan gambar-gambar visual yang berwarna-warni dan dalam bentuk yang lucu, hal ini membuktikan bahwa visualisasi data dalam pembelajaran sangat berpengaruh baik untuk kalangan balita, batita, remaja, dewasa, bahkan untuk orang yang sudah sepuhvisualisa sekalipun"

# Click on the current mouse position and type the message
for a in range(10):
    pyautogui.click(position.x, position.y)
    pyautogui.write(pesan)  # Use pyautogui.write() to type the message
    print(pesan)
    time.sleep(0.1)
    pyautogui.press("enter")  # Use pyautogui.press() to simulate pressing the "enter" key





