import sys
import webbrowser

arguments = sys.argv

def get_directions(arguments):

    destinations = arguments[1:]

    base_url = "https://www.google.co.uk/maps/dir/"
    final_url = ""

    if len(destinations) > 1 and len(destinations) < 11:
        final_url = base_url
        
        for destination in destinations:
            final_url += str(destination + "/")
        
        webbrowser.get('chrome').open_new_tab(final_url)
        
    else:
        error_message = "Error: Number of locations should be greater than 1 and less than 11"
        print(error_message)

        return error_message

    return final_url

get_directions(arguments)

# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array