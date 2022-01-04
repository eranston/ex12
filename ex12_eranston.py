def find_length_n_paths(n,board,words):
    



    check_posibble_move(board , path)





def recursion_path_finder(n , board ,current_path,  path_lst , words):

    
    if n == 0:
        if is_valid_path(board , current_path , words) is None:
            return []

        else:
            return current_path

    



    do_all_moves(n ,board , current_path , path_lst)

    

def do_move(move , current_path , n , board , path_lst):
   
    current_path.append(move)
    path_temp = recursion_path_finder(n-1 , board , current_path , path_lst  )
    if len(path_temp) != 0:

        path_lst.append(path_temp)
    current_path.pop()


def do_all_moves(n ,  board, current_path , path_lst):

    current_row = current_path[-1][0]
    current_col = current_path[-1][1]

    for i in range(-1,2):
        for j in range(-1,2):
            do_move((current_row + i , current_col + j) , current_path ,  n, board , path_lst)

    

    