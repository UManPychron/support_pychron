'''
mass spec equivalent
Message "Expand Pipette 2"
Close "Minibone to Turbo"
Delay 2
Open "Outer Pipette 2"
BeginInterval 15
CompleteInterval
'''
def main():
    info('Expand Pipette 2')
    close(description='Minibone to Turbo')
    sleep(2)
    open(description='Outer Pipette 2')
    sleep(15)
