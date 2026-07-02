import cv2 as cv, numpy as np
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load_screenshot(image_path):
    image = cv.imread(image_path)  # Reads the image from disk
    return image

def find_minable_ore():
    screenshot_path = os.path.join(BASE_DIR, "game_screenshot.png")
    template_path = os.path.join(BASE_DIR + "/assets/templates", "obsidian_ore.png")
    screenshot = load_screenshot(screenshot_path)
    template = cv.imread(template_path)
    result = cv.matchTemplate(screenshot, template, cv.TM_CCOEFF_NORMED)

    threshold = 0.8
    locations = cv.minMaxLoc(result)
    
    if locations[1] > threshold:
        print("ore found at", locations[3])  # Location of the match
        return locations[3]  # The top-left corner of the match
    else:
        print("ore not found")
        return None
    

def search_for_x(thing):
    screenshot_path = os.path.join(BASE_DIR + "/assets/screenshots/game_screenshot.png")
    template_path = os.path.join(BASE_DIR + "/assets/templates" + f"{thing}.png")
    screenshot = load_screenshot(screenshot_path)
    template = load_screenshot(template_path)
    
    # Match the template to the screenshot
    result = cv.matchTemplate(screenshot, template, cv.TM_CCOEFF_NORMED)
    
   
    threshold = 0.7
    locations = np.where(result >= threshold)  # Get all locations that match above the threshold
    
    # Convert the locations into rectangles (x, y, width, height)
    rectangles = []
    for pt in zip(*locations[::-1]):  # Switch x and y for correct order
        rectangles.append((pt[0], pt[1], template.shape[1], template.shape[0]))
    
    # Apply Non-Maximum Suppression to remove redundant matches
    rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.2)
    
    # Count how many unique matches we have after suppression
    match_count = len(rectangles)
    
    print(f"Found {match_count} matches in the image!")
    
    # Optionally, if you want to visualize the matches:
    for (x, y, w, h) in rectangles:
        cv.rectangle(screenshot, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Resize the image to fit the screen (adjust the scaling factor as needed)
    height, width = screenshot.shape[:2]
    scaling_factor = 0.5  # Change this value to make the image smaller or larger
    resized_screenshot = cv.resize(screenshot, (int(width * scaling_factor), int(height * scaling_factor)))
    
    # Show the image with rectangles drawn around the matches
    cv.imshow("Matches", resized_screenshot)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return match_count


