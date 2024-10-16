import pandas as pd

import streamlit as st

# import crawler

class Listings:
    
    def __init__(self, listings_path: str):
        
        self.listings_df = pd.read_csv(listings_path, parse_dates=['date'])

    def display_listings(self):

        table_style = """
        <style>
        table {
            width: 100%;
            border-collapse: collapse;
            font-family: 'Roboto', sans-serif;
            font-size: 14px;
        }
        th {
            background-color: #f0f2f6;
            color: #333;
            text-align: left;
            padding: 12px;
            border-bottom: 2px solid #ddd;
        }
        td {
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }
        tr:hover {background-color: #f5f5f5;}
        a {
            color: #1f77b4;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        </style>
        """
        
        # Create an HTML table with clickable titles
        table_html = """
        <table>
        <tr>
            <th>Portal</th>
            <th>Data</th>
            <th>Anunci</th>
        </tr>
        """

        # Add each row with the title linked
        for i in range (len(self.listings_df)):

            source = self.listings_df.loc[i, 'source']
            date = self.listings_df.loc[i, 'date']
            link = self.listings_df.loc[i, 'link']
            title = self.listings_df.loc[i, 'title']
            
            # Add the row to the HTML table with the title linked and other columns
            table_html += f"""
            <tr>
                <td>{source}</td>
                <td>{date}</td>
                <td>
                    <a href="{link}" target="_blank">{title}</a>
                </td>
            </tr>
            """

        # Close the HTML table tag
        table_html += "</table>"

        # Combine the custom CSS with the table HTML
        full_html = table_style + table_html

        # Display the table
        st.components.v1.html(full_html, height=500, scrolling=True)

def main():

    st.set_page_config(
        page_title='Anuncis de Particulars',
        page_icon="🏡",
        layout='wide',
        initial_sidebar_state='auto' # hides the sidebar on small devices and shows it otherwise
    )

    st.title("🏡 Anuncis de Particulars")
    st.write("""
    
    """)

    listings = Listings("listings/listings.csv")
    listings.display_listings()


if __name__ == "__main__":
    main()