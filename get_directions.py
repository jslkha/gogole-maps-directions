import sys
import webbrowser

base_url = "https://www.google.co.uk/maps/dir/"
destinations = sys.argv

if len(sys.argv) > 3:
    final_url = base_url + destinations[1] + "/" + destinations[2] + "/" + destinations[3]
    print(final_url)
    
    webbrowser.get('chrome').open_new_tab(final_url)
else:
    print("Inefficient number of arguments")
