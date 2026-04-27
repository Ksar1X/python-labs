import pandas as pd
import pickle

file_name = "richest_movie"
folder_path = "D:\\python-labs\\6-python-lab\\task2\\movies.csv"

def find_and_save_richest_bw_movie(csv_path, pickle_path):
    try:
        data = pd.read_csv(csv_path, encoding='utf-8')
        dfs = pd.DataFrame(data)
        baw_movies = dfs[dfs['color'] == " Black and White"]
        richest_movies = baw_movies.loc[baw_movies['budget'].idxmax()]
        movie_title = richest_movies["movie_title"]
        print(f'Black and white film with biggest budget: {movie_title}')

        with open(pickle_path, "wb") as file:
            pickle.dump(data, file)
        print("Data has been saved in file!")

    except FileNotFoundError:
        print("File not found!")
    except KeyError:
        print("Something went wrong!")
    except Exception as e:
        print(e)

find_and_save_richest_bw_movie(folder_path, file_name)