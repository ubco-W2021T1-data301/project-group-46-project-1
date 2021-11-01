import numpy as np\n",
import pandas as pd\n",
import matplotlib.pylab as plt
import seaborn as sns    #Understanding my variables\n",
    
    def first_python_module(url_or_path_to_csv_file):
    
       # Method Chain 1 (Load data,rename columns, get rid of null values and drop necessary data with missing data)\n",
    
        df1 = (
                pd.read_csv(url_or_path_to_csv_file)\n",
               .drop(['NBA_FLAG','JERSEY','PIE','TEAM_ABBREVIATION','TEAM_ID','ALL_STAR_APPEARANCES','GAMES_PLAYED_CURRENT_SEASON_FLAG','FROM_YEAR','TO_YEAR','DLEAGUE_FLAG','TEAM_CODE','TEAM_CITY','DISPLAY_FIRST_LAST','PLAYER_SLUG','FIRST_NAME','LAST_NAME','DISPLAY_FI_LAST','GAMES_PLAYED_FLAG','PLAYERCODE'], axis=1)\n",
               .rename(columns={'DISPLAY_LAST_COMMA_FIRST': 'FULL NAME', 'PTS':'PPG', 'AST':'APG','REB':'RBG'})\n",
               .dropna(axis=0)
                
          )
    
        return df1
  
  
    ## I want to find out the tallest best player and shortest best player\n",
    ## I used just one dataset because it had most of the information I was looking for and was appropriate enough.\n",
    ##   I removed columns that I found to be redundant and useless and also renamed some so I would have a better   understanding of it. I experimented with just a few data visualizations which I still think I should do more of so I can accurately answer my question to a tee. "
  
