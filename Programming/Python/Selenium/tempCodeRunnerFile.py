    print("Sleeping")
    time.sleep(10)
    print("Sleep Done")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,"nextButton"))) 
    element.click()
    print("Clicked")