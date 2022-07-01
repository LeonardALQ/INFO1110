from little_battle import load_config_file
# Don't remove any comments in this file
folder_path = "./invalid_files/"

# Please create appropriate invalid files in the folder "invalid_files"
# for each unit test according to the comments below and
# then complete them according to the function name

def test_file_not_found():
  # no need to create a file for FileNotFound
  try: 
    load_config_file(folder_path + "No_file.txt")
    error_detected = False 
  except FileNotFoundError: 
    error_detected = True 
  except: 
    error_detected = False 
  
  assert error_detected, "File Not Found Error went undetected"
  if error_detected: 
    print("Passed: file not found.")

def test_format_error():
  # add "format_error_file.txt" in "invalid_files"
  expected_error = SyntaxError("Invalid Configuration File: format error!")
  fail_msg = "Test format error went undetected"
  try: 
    load_config_file(folder_path + "test_format_error.txt")
  except SyntaxError as err: 
    assert str(expected_error) == str(err), fail_msg
    print("Passed: format error.")
  except: 
    print(fail_msg)

def test_frame_format_error():
  # add "frame_format_error_file.txt" in "invalid_files"
  expected_error = SyntaxError("Invalid Configuration File: frame should be in format widthxheight!")
  fail_msg = "Test frame format error went undetected"
  try: 
    load_config_file(folder_path + "frame_format_error_file.txt")
  except SyntaxError as err: 
    assert str(expected_error) == str(err), fail_msg
    print("Passed: frame format error.")
  except: 
    print(fail_msg)

def test_frame_out_of_range():
  # add "format_out_of_range_file.txt" in "invalid_files"
  expected_error = ArithmeticError("Invalid Configuration File: width and height should range from 5 to 7!")
  fail_msg = "Test frame out of range error went undetected"
  try: 
    load_config_file(folder_path + "format_out_of_range_file.txt")
  except ArithmeticError as err: 
    assert str(expected_error) == str(err), fail_msg
    print("Passed: frame out of range.")
  except: 
    print(fail_msg)

def test_non_integer():
  # add "non_integer.txt" in "invalid_files"

  expected_error = ValueError("Invalid Configuration File: Water contains non integer characters!")
  fail_msg = "Test non integer went undetected"
  try: 
    load_config_file(folder_path + "non_integer.txt")
  except ValueError as err: 
    assert str(expected_error) == str(err), fail_msg
    print("Passed: non integer.")
  except: 
    print(fail_msg)

def test_out_of_map():
  expected_error = ArithmeticError("Invalid Configuration File: Gold contains a position that is out of map.")
  fail_msg = "Test out of map went undetected"
  try: 
    load_config_file(folder_path + "out_of_map.txt")
  except ArithmeticError as err: 
    assert str(expected_error) == str(err), fail_msg
    print("Passed: out of map.")
  except: 
    print(fail_msg)

def test_occupy_home_or_next_to_home():
  expected_error = ValueError("Invalid Configuration File: The positions of home bases or the base positions next to the home bases are occupied!")
  fail_msg = "Test occupy home or next to home went undetected"
  try: 
    load_config_file(folder_path + "occupy_home_or_next_to_home.txt")
  except ValueError as err: 
    assert str(expected_error) == str(err), fail_msg
    print("Passed: occupy home or next to home.")
  except: 
    print(fail_msg)

def test_duplicate_position():
  # add two files: "dupli_pos_in_single_line.txt" and
  expected_error = SyntaxError("Invalid Configuration File: Duplicate position (0, 0)!")
  fail_msg = "Test duplicate position went undetected"
  try: 
    load_config_file(folder_path + "dupli_pos_in_single_line.txt")
  except SyntaxError as err: 
    assert str(expected_error) == str(err), fail_msg
  except: 
    print(fail_msg)

  # "dupli_pos_in_multiple_lines.txt" in "invalid_files"
  expected_error = SyntaxError("Invalid Configuration File: Duplicate position (2, 2)!")
  fail_msg = "Test duplicate position went undetected"
  try: 
    load_config_file(folder_path + "dupli_pos_in_multiple_lines.txt")
  except SyntaxError as err: 
    assert str(expected_error) == str(err), fail_msg
    print("Passed: duplicate position.")
  except: 
    print(fail_msg)

def test_odd_length():
  # add "odd_length_file.txt" in "invalid_files"
  expected_error = SyntaxError("Invalid Configuration File: Water has an odd number of elements!")
  fail_msg = "Test duplicate position went undetected"
  try: 
    load_config_file(folder_path + "odd_length_file.txt")
  except SyntaxError as err: 
    assert str(expected_error) == str(err), fail_msg
    print("Passed: odd length.")
  except: 
    print(fail_msg)

def test_valid_file():
  assert load_config_file("config.txt") == (
    5, 5, 
    [(0, 0), (4, 2), (1, 3)], [(0, 2), (2, 4)], 
    [(0, 4), (3, 1)], 
    [(4, 1), (2, 2)], 
    #This is an extra array that I return in the function for my code.
    [(1, 1), (0, 1), (1, 0), (2, 1), (1, 2), (3, 3), (2, 3), (3, 2), (4, 3), (3, 4)]
  ), "Configuration file not loaded correctly"
  print("Passed: valid file.")

# you can run this test file to check tests and load_config_file
if __name__ == "__main__":
  test_file_not_found()
  test_format_error()
  test_frame_format_error()
  test_frame_out_of_range()
  test_non_integer()
  test_out_of_map()
  test_occupy_home_or_next_to_home()
  test_duplicate_position()
  test_odd_length()
  test_valid_file()
