import csv
import matplotlib.pyplot as plt


def generate_summary_for_web(csvfile, html_title, html_filename, show_barchart_gender=True):
    """
    Reads csv file and generates html file containing summary table and, if show_barchart_gender is True,
    barchart gender image
    """
    # lists to store accumulated data for each case
    yes_positive = [0 for i in range(14)]
    yes_negative = [0 for i in range(14)]
    no_positive = [0 for i in range(14)]
    no_negative = [0 for i in range(14)]
    m_negative = 0
    f_negative = 0
    m_positive = 0
    f_positive = 0

    with open(csvfile, "r") as f_obj:

        reader = csv.reader(f_obj)
        # read header
        header = next(reader)
        header = header[2:16]
        # read and accumulate data
        for row in reader:
            if row[16] == "Positive":
                if row[1] == "Male":
                    m_positive += 1
                elif row[1] == "Female":
                    f_positive += 1
                for i in range(14):
                    if row[i + 2] == "Yes":
                        yes_positive[i] += 1
                    elif row[i + 2] == "No":
                        no_positive[i] += 1
            elif row[16] == "Negative":
                if row[1] == "Male":
                    m_negative += 1
                elif row[1] == "Female":
                    f_negative += 1
                for i in range(14):
                    if row[i + 2] == "Yes":
                        yes_negative[i] += 1
                    elif row[i + 2] == "No":
                        no_negative[i] += 1

    #  create table body string for html file
    table_string = ""
    for i in range(14):
        table_string += "\t\t\t\t<tr>\n"
        table_string += "\t\t\t\t\t<td> " + header[i].capitalize() + " </td>\n"
        table_string += "\t\t\t\t\t<td> " + str(yes_positive[i]) + " </td>\n"
        table_string += "\t\t\t\t\t<td> " + str(no_positive[i]) + " </td>\n"
        table_string += "\t\t\t\t\t<td> " + str(yes_negative[i]) + " </td>\n"
        table_string += "\t\t\t\t\t<td> " + str(no_negative[i]) + " </td>\n"
        table_string += "\t\t\t\t</tr>\n"

    # create image string for html file
    img_string = ""
    if show_barchart_gender:
        generate_barchart_gender(m_positive, m_negative, f_positive, f_negative)
        img_string = """<img src="barchart_gender.png" alt="" />"""

    # create string for html file
    html_string = """
<!DOCTYPE html> 
<html>
    <head>
        <meta charset = "UTF-8">  
        <style>
            table
            {
                border-spacing:0;
                border-collapse:collapse;
            }
            td
            {
                border:2px solid black;
            }
    
            tbody tr:nth-child(odd)
            {
                background-color:grey;
            }
    
            tbody tr:nth-child(even)
            {
                background-color:white;
            }
        </style>
        
        <title> """ + html_title + """ </title>
    </head>

    <body>
        <h1> """ + html_title + """  </h1>
        <div style="display:flex"> 
        <table>
            <thead>
                <tr>
                    <td rowspan = "3" style="text-align:center"> Atributes </td>
                    <td colspan = "4" style="text-align:center"> Class </td>
                </tr>
                <tr>
                    <td colspan = "2"> Positive </td>
                    <td colspan = "2"> Negative </td>            
                </tr>
                <tr>
                    <td> Yes </td>
                    <td> No </td>
                    <td> Yes </td>
                    <td> No </td>
                </tr>
            </thead>
            
            <tbody> \n""" + table_string + """      
            </tbody>
        </table>
        
        """ + img_string + """
        </div>
    </body>
</html>"""

    f = open(html_filename, 'w')
    f.write(html_string)


def generate_barchart_gender(m_positive, m_negative, f_positive, f_negative):
    """
    Generates barchart_gender image and save it in 'barchart_gender.png' file
    :param m_positive:number of positive case for male
    :param m_negative:number of negative case for male
    :param f_positive:number of positive case for female
    :param f_negative:number of negative case for female
    :return:None
    """

    # data to plot
    male = (m_positive, m_negative)
    female = (f_positive, f_negative)

    # create plot
    plt.subplots()
    bar_width = 0.35
    opacity = 0.8
    index1 = [0, 1]
    index2 = [bar_width, 1 + bar_width]
    index3 = [bar_width / 2, 1 + bar_width / 2]

    plt.bar(index1, male, bar_width, alpha=opacity, color='b', label='Male')

    plt.bar(index2, female, bar_width, alpha=opacity, color='orange', label='Female')

    plt.xlabel('Class')
    plt.ylabel('Count')
    plt.title('Gender of Positive vs Negatives case')
    plt.xticks(index3, ('Positive', 'Negative'))
    plt.legend()

    plt.tight_layout()

    # save plot to file
    plt.savefig('barchart_gender.png')
    # plt.show()
