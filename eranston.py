def find_length_n_paths(n,board,words):
    



    check_posibble_move(board , path)





def recursion_path_finder(n , board ,current_path,  path_lst):

    
    if n == 0:
        return current_path

    if check_posibble_move(board, current_path) is False:
        return []



    current_row = current_path[-1][0]
    current_col = current_path[-1][1]
    current_path.append(current_row , current_col)
    path_lst.append(recursion_path_finder(n-1 , board , current_path , path_lst  ))





def check_posibble_move(board, path):
    pass