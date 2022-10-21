
# Starting text
print('Welcome to AutoVS, an easy way to format your Aeronautica Vehicle Suggestions!' + '\n'
'Press ENTER to continue.')
input()

# Input Options
print('There are two formatting options:' + '\n'
'1 - Peformance ONLY' + '\n'
'2 - Complete (Characteristics & Peformance)' + '\n'
'To select an option, either type "1" or "2" and press ENTER.')

format = input() # Variable for the user's input.

if format == '1':
    print("Tip: If the source doesn't specify a parameter, use 'N/A', or 'Not mentioned.'." + '\n')

    Plane = input('Plane name? ') # Plane name 
    BasicInfo = input('Summarized info about said aircraft? ') # Basic info about the plane
    
    Max = input('Max speed? ') # Max speed
    Stall = input('Stall / Landing speed? ') # Stall / Landing speed 
    Range = input('Range? ') # Range of the aircraft
    Ceiling = input('Service ceiling? ') # Service ceiling of the aircraft
    
    Wikipedia = input('Wikipedia link? ') # Wikipedia link

    print("Would you like it bolded and italicized?" + '\n'
    '1 - Yes' + '\n'
    '2 - No' + '\n')
   
    option1 = input()

    if option1 == '1':
        # Final Document | Output
        print('\n'
        '**' + Plane + '**', '('+ BasicInfo +')' + '\n'
        '' + '\n'
        '**Specs**' + '\n'
        '' + '\n' 
        '— *Performance:*' + '\n'
        '- Max speed:', Max + '\n'
        '- Stall / Landing speed:', Stall + '\n'
        '- Range:', Range + '\n'
        '- Ceiling', Ceiling + '\n'
        '' + '\n'
        '**Wikpedia Link:**', Wikipedia + '\n'
        )

    elif option1 == '2':
        print('\n',
        Plane, '('+ BasicInfo +')' + '\n'
        '' + '\n'
        'Specs' + '\n'
        '' + '\n' 
        '— Performance:' + '\n'
        '- Max speed:', Max + '\n'
        '- Stall / Landing speed:', Stall + '\n'
        '- Range:', Range + '\n'
        '- Ceiling', Ceiling + '\n'
        '' + '\n'
        'Wikpedia Link:', Wikipedia + '\n')

# Barrier to remove confusion

elif format == '2':

    print("Tip: If the source doesn't specify a parameter, use 'N/A', or 'Not mentioned.'." + '\n')

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
    
    Wikipedia = input('Wikipedia link? ') # Wikipedia link

    print("Would you like it bolded and italicized?" + '\n'
    '1 - Yes' + '\n'
    '2 - No' + '\n')
    
    option2 = input()

    if option2 == "1":
    # Final document | Output
        print('**' + Plane + '**', '('+ BasicInfo +')' + '\n'
        '' + '\n'
        '**Specs**' + '\n'
        '' + '\n'
        '— *Characteristics:*' + '\n'
        '- Crew:', Crew + '\n'
        '- Capacity:', Crew + '\n'
        '- Length"', Length + '\n'
        '- Width:', Width + '\n'
        '- Wingspan:', Wingspan + '\n'
        '- Height:', Height + '\n'
        '' + '\n'
        '— *Performance:*',
        '- Max speed:', Max + '\n'
        '- Stall / Landing speed:', Stall + '\n'
        '- Range:', Range + '\n'
        '- Service Ceiling', Ceiling  + '\n'
        '**Wikipedia Link:**', Wikipedia + '\n'
        )

    elif option2 == "2":
       print(Plane, '('+ BasicInfo +')' + '\n'
        '' + '\n'
        'Specs' + '\n'
        '' + '\n'
        '— Characteristics:' + '\n'
        '- Crew:', Crew + '\n'
        '- Capacity:', Crew + '\n'
        '- Length"', Length + '\n'
        '- Width:', Width + '\n'
        '- Wingspan:', Wingspan + '\n'
        '- Height:', Height + '\n'
        '' + '\n'
        '— Performance:',
        '- Max speed:', Max + '\n'
        '- Stall / Landing speed:', Stall + '\n'
        '- Range:', Range + '\n'
        '- Service Ceiling', Ceiling  + '\n'
        'Wikipedia Link:', Wikipedia + '\n'
        )

print('Your suggestion has been loaded! Thank you for using AutoVS.' + '\n' # Aesthetic 
'To make another suggestion, reload this file.') # Helpful suggestion

# END