# happy_stubs.py


def main():
    
    # Part 1
    # Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()

    # Part 2
    # Print key value pairs sorted by key
    # Uncomment the function call below for part 2 only
    ##print_sorted_dictionary(happy_dict)

    # Part 3
    # Uncomment the function call below for part 3 only
    # lookup happiness by country until the user enters done
    #lookup_happiness_by_country(happy_dict)

    # Parts 4-6
    # Uncomment the function call below for parts 4-6 
    # Read file containing population and GDP data and add happiness data
    read_gdp_data(happy_dict)



def make_happy_dict():
    ##creates a dictionary
    dict_list = {}
    ##opens file as read 
    file = open("happiness.csv","r")
    ##reads first line to ignore header
    file.readline()
    ##for loops goes through each line stripping empty space and spliting on ","
    for line in file:
        line = line.strip("\n")
        line = line.split(",")
        ###assigns the happy index as the 3rd item in the split
        happy_index = line[2]
        ###assigns the country as the 1st item in the split
        country = line[0]
        ##assigns values to the dictionary variable
        dict_list[country] = happy_index
    ##prints the dict list
    ##print(dict_list)
    ###closes file
    file.close()
    ###returns the dict values
    return dict_list

def read_gdp_data(happy_dict):  
    ##opens file as read 
    file = open("world_pop_gdp.tsv","r")
    ##reads first line to ignore header
    first_line = file.readline()
    ###replaces spaces with commas
    first_line = first_line.replace("\t", ",")
    ## reprints first line with no space at end
    print(first_line, end = "")
    ##for loops goes through each line 
    for line in file:
        ##strips empty space
        line.strip()
        ##replaces each lines dollar sign with empty space
        line = line.replace("$", "")
        ##replaces each lines comma sign with empty space
        line = line.replace(",", "")
        ### splits each part based on space
        line = line.split("\t")
        ### assigns contry to first index of split
        country = line[0]
        ##assigns population to 2nd index of split
        population = line[1]
        ##assigns gdp to third index of split
        gdp = line[2]
        ###replaced the 3rd index commas, with empty space
        gdp = gdp.replace(",","")
        ## prints out new index with commas inbetween and no space at end
        print(country+","+population+","+gdp, end = "")

def lookup_happiness_by_country(happy_dict):
    ###While true loop
    while True:
        ##asks the country's name or done to stop
        ask = input("Enter a country to lookup or 'done' to exit:")
        ## if the input is done, we leave the loop and are done
        if ask == "done":
            return 
        ## if input is in the happy_dict, it prints out the value assosianted with it
        if ask in happy_dict:
            print(happy_dict[ask])
        ## if a input is not in happy_dict or is not done, prints not found 
        else:
            print(ask,"not found")

# Function prints all the values in a dictionary d sorted by key
def print_sorted_dictionary(D):
    if type(D) != type({}):
        print("Dictionary not found")
        return
    print("Contents of dictionary sorted by key.")
    print("Key","Value")
    for key in sorted(D.keys()):
        print(key, D[key])
        
main()
