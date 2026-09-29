# PWM Generator
# Simple Python simulation of a PWM signal

def generate_pwm(duty_cycle, frequency, cycles):
    if duty_cycle < 0 or duty_cycle > 100:
        print("Duty cycle must be between 0 and 100%")
        return

    if frequency <= 0:
        print("Frequency must be greater than 0")
        return

    print("\nPWM Signal:")
    print("-" * 40)

    total_steps = 20
    high_steps = int((duty_cycle / 100) * total_steps)

    for cycle in range(cycles):
        signal = "█" * high_steps + "_" * (total_steps - high_steps)
        print(f"Cycle {cycle + 1}: {signal}")

    print("\nPWM Parameters:")
    print(f"Frequency   : {frequency} Hz")
    print(f"Duty Cycle  : {duty_cycle}%")
    print(f"Cycles      : {cycles}")


# Main program
duty_cycle = float(input("Enter duty cycle (%): "))
frequency = float(input("Enter frequency (Hz): "))
cycles = int(input("Enter number of cycles: "))

generate_pwm(duty_cycle, frequency, cycles)
