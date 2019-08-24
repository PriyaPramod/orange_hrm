

def switch_to_child_window(driver):
    child_window = None
    parent_window = driver.current_window_handle
    window_ids = driver.window_handles
    try:
        for window_id in window_ids:
            if window_id != parent_window:
                child_window = window_id
                break
        driver.switch_to.window(child_window)
    except Exception:
        print("Unable to change the focus to the child window")
