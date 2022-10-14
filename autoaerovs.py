
# Starting text
print('Welcome to AutoVS, an easy way to format your Aeronautica Vehicle Suggestions!')
print('Press ENTER to continue.')
input()

# Input Options
print('There are two formatting options:')
print('1 - Peformance ONLY  ')
print('2- Complete (Characteristics & Peformance)')
print('To select an option, either type "1" or "2" and press ENTER.')

option = input() # Variable for the user's input.

yes = 'Privyet, Papa.' # testing variable

if option == '1':
    print("Tip: If the source doesn't specify a parameter, use 'N/A', or 'Not mentioned.'.")
    
    Plane = input('Plane name? ') # Plane name 
    BasicInfo = input('Summarized info about said aircraft? ') # Basic info about the plane
    
    Max = input('Max speed in knots? ') # Max speed
    Stall = input('Stall / Landing speed in knots? ') # Stall / Landing speed 
    Range = input('Range in KM and NMI? ') # Range of the aircraft
    Ceiling = input('Service ceiling in FT and M? ') # Service ceiling of the aircraft
    
    Wikipedia = input('Wikipedia link?') # Wikipedia link

    # Printing | Output
    print('**',Plane,'**', '(',BasicInfo,')')
    print('')
    print('**Specs**')
    print('')
    print('- *Performance*')
    print('- 100%:', Max)
    print('- Stall/Landing', Stall)
    print('- Range', Range)
    print('- Ceiling', Ceiling)
    print('')
    print('**Wikipedia Link:**', Wikipedia)

    print('Your suggestion has been loaded! Thank you for using AutoVS.') # Aesthetic 
    print('To make another suggestion, reload this file.') # Helpful suggestion

elif option == '2':

    print("Tip: If the source doesn't specify a parameter, use 'N/A', or 'Not mentioned.'.")
    
    Plane = input('Plane name? ') # Plane name 
    BasicInfo = input('Summarized info about said aircraft? ') # Basic info about the plane
    
    Crew = input('Crew? ') # Crew
    Cap = input('Capacity? ') # Capacity
    Length = input('Length? ') # Length
    Width = input('Width? ') # Width 
    Wingspan = input('Wingspan? ') # Wingspan
    Height = input('Height? ') # Height

    Max = input('Max speed in knots? ') # Max speed
    Stall = input('Stall / Landing speed in knots? ') # Stall / Landing speed 
    Range = input('Range in KM and NMI? ') # Range of the aircraft
    Ceiling = input('Service ceiling in FT and M? ') # Service ceiling of the aircraft
    
    Wikipedia = input('Wikipedia link?') # Wikipedia link

    # Final document | Output
    print('**',Plane,'**', '(',BasicInfo,')')
    print('')
    print('**Specs**')
    print('')
    print('— *Characteristics:*')
    print('-', 'Crew:', Crew)
    print('-', 'Capacity:', Cap)
    print('-', 'Length:', Length)
    print('-', 'Width:', Width)
    print('-', 'Wingspan:', Wingspan)
    print('-', 'Height:', Height)
    print('')
    print('— *Performance:*')
    print('-', 'Max speed:', Max)
    print('-', 'Stall / Landing speed:', Stall)
    print('-', 'Range:', Range)
    print('-', 'Ceiling', Ceiling)
    print('',)
    print('**Wikipedia Link**', Wikipedia)

    print('Your suggestion has been loaded! Thank you for using AutoVS.') # Aesthetic 
    print('To make another suggestion, reload this file.') # Helpful suggestion

    # END