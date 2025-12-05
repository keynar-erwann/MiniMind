import pandas as pd
import matplotlib.pyplot as plt


# # reading the database
# data = pd.read_csv("tips.csv")

# # Scatter plot with day against tip
# plt.scatter(data['day'], data['tip'], c=data['size'], 
#             s=data['total_bill'])

# # Adding Title to the Plot
# plt.title("Scatter Plot")

# # Setting the X and Y labels
# plt.xlabel('Day')
# plt.ylabel('Tip')

# plt.colorbar()

# plt.show()



def scatter_plot_data(title : str ) -> None :
    """ 
    This function allows you to visualize a scatter plot using the tips.csv file 

    Args : 

  title : the title of the plot eg, "Scatter Plot"

    """
    data = pd.read_csv("tips.csv")
    plt.scatter(data['day'], data['tip'], c=data['size'], 
            s=data['total_bill'])
    plt.title(title)
    plt.xlabel('Day')
    plt.ylabel('Tip')
    plt.colorbar()

    plt.show()




def bar_chat_data(title : str) -> None :
    """  This function allows you to visualize a bar chat using the tips.csv file 

    Args : 

  title : the title of the plot eg, "Bar Chat"
    """
    data = pd.read_csv("tips.csv")


    plt.bar(data['day'], data['tip'])

    plt.title(title)


    plt.xlabel('Day')
    plt.ylabel('Tip')


    plt.show()




