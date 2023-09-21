import subprocess 

exit_program = False

def connect_device(ip_address):
    subprocess.run(f"adb connect {ip_address}:5555", shell=True)
    
def disconnect_device(ip_address):
    subprocess.run(f'adb disconnect', shell=True)

def check_device_connection():
    result = subprocess.run("adb devices",shell=True, stdout=subprocess.PIPE, text=True)
    return "5555" in result.stdout

def is_droidcam_running():
    # Menggunakan "adb shell ps" untuk mendapatkan daftar proses yang berjalan di perangkat
    result = subprocess.run("adb shell ps", shell=True, stdout=subprocess.PIPE, text=True)
    # Mencari kata "com.dev47apps.droidcam" dalam daftar proses
    return "com.dev47apps.droidcam" in result.stdout

print(f"{'='*20} Hubungkan Perangkat {'=' * 20}")
ip_address = input('alamat ip :')

if not check_device_connection():
    print('perangkat tidak terhubung. Menyambungkan ulang...')
    connect_device(ip_address)
 
try :
    while not exit_program:
        print (f"{'*' * 20} APLICATION {'*' * 20}")
        print('1. All Control')
        print('2. Live front cam')
        print('3. Camera')
        print('4. Pull Data')
        print('0. Close Program')
        aplication = int(input('pilih aplikasi : '))

        if aplication == 1 :
            print(f"{'=' * 50} Menu {'=' * 50}")
            print('1. Download Aplikasi')
            print('2. Jalankan Aplikasi')
            print('3. Hentikan Aplikasi')
            print('4. Uninstall Aplikasi')
            print('0. Break')

            while True :
                menu = int(input('pilih : '))

                if menu == 1 :
                    print('mendownload aplikasi')
                elif menu == 2 :
                    if not is_droidcam_running():
                        subprocess.run('adb shell am start -n com.dev47apps.droidcam/com.dev47apps.droidcam.DroidCam', shell=True)
                    else:
                        print('DroidCam sudah berjalan')
                elif menu == 3 :
                    subprocess.run('adb shell am force-stop com.dev47apps.droidcam', shell=True)
                elif menu == 4 :
                    print('Uninstall Aplikasi')
                elif menu == 0 :
                    break     
                   
        elif aplication == 3 :
            kamera = "android.media.action.VIDEO_CAPTURE"
            command = f"adb shell am start -a {kamera}"
            subprocess.run(command, shell=True)

            print(f"{'*' * 20} SILAHKAN LAKUKAN TINDAKAN ANDA {'*' * 20}")
            print('1. Tekan 1 untuk mengambil gambar')
            print('2. Berhenti mengambil rekaman')
            print('3. Simpan hasil foto')
            print('4. Lihat foto')
            print('0. Tekan untuk keluar')

            while True:
                userListener = int(input('pilih tindakan anda : '))

                if userListener == 1 :
                    startCaptureImage = f'adb shell input tap 500 2000'
                    subprocess.run(startCaptureImage, shell=True)
                elif userListener == 2 :
                    stopCaptureImage = f'adb shell input tap 500 2000'
                    subprocess.run(stopCaptureImage, shell=True)
                elif userListener == 3 :
                    saveCaptureImage = f'adb shell input tap 800 2000'
                    subprocess.run(saveCaptureImage, shell=True)
                elif userListener == 4 :
                    showCaptureImage = 'adb pull /sdcard/DCIM/Camera/ ~/Desktop/Android'
                    subprocess.run(showCaptureImage,shell=True)
                elif userListener == 0 :
                    break
                else:
                    print('tindakan tidak valid !! silahkan pilih kembali')

        elif aplication == 0 :
            exit_program = True
        
except KeyboardInterrupt :
    pass
finally:
    disconnect_device()
    print('Program Ditutup')