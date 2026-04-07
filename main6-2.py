from gpiozero import Buzzer, DigitalInputDevice
import time

# 1. 하드웨어 객체 생성 (부저: GPIO 18, 가스 센서: GPIO 17)
bz = Buzzer(18)
gas = DigitalInputDevice(17)

try:
    print("Gas/Smoke Detection System Started...")
    while True:
        # 2. 가스 센서의 상태값 확인
        # gas.value가 0이면 가스 감지(LOW), 1이면 정상(HIGH) 상태를 의미함
        if gas.value == 0: 
            # ← 0 = 가스 감지 (가스 유입 시 센서 저항 감소로 인한 LOW 신호 발생)
            print("⚠️ 가스 감지됨 (Gas Detected!)")
            bz.on()   # 부저 가동 (경고음 발생)
        else: 
            # ← 1 = 정상 상태 (공기 중 산소 흡착으로 인한 HIGH 신호 유지)
            print("✅ 정상 (Normal)")
            bz.off()  # 부저 정지

        # 3. 0.2초 간격으로 센서 데이터를 샘플링하여 실시간 모니터링 수행
        time.sleep(0.2)

except KeyboardInterrupt:
    # 사용자가 Ctrl+C를 눌러 강제 종료할 때 예외 처리
    print("\n[System] 프로그램을 종료합니다.")
    pass

# 4. 프로그램 종료 시 부저를 확실히 끄고 자원 정리
bz.off()
