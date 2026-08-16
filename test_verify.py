from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 390, "height": 844})

    file_url = f"file://{os.path.abspath('pump.html')}"
    page.goto(file_url)
    page.wait_for_timeout(1000)

    os.makedirs("/home/jules/verification", exist_ok=True)

    # Bypass firebase loading screen / home stack setup
    page.evaluate("""() => {
      document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
      document.getElementById('screen-home').classList.add('active');
      document.getElementById('homeStack').innerHTML = `
        <div class="btn-pill" onclick="goToExerciseSelect('level')">LEVEL MODE</div>
        <div class="btn-pill" onclick="openMatchModeModal()">ONLINE MATCH</div>
        <div class="btn-pill btn-pill-yellow" onclick="goTo('leaderboard')">LEADERBOARD</div>
      `;
    }""")
    page.wait_for_timeout(300)
    page.screenshot(path="/home/jules/verification/01_home.png")

    # Click ONLINE MATCH button directly using evaluate or locator
    page.click("text=ONLINE MATCH")
    page.wait_for_timeout(300)
    page.screenshot(path="/home/jules/verification/02_match_mode_modal.png")

    # Click JOIN ROOM -> opens PIN pad modal
    page.click("text=JOIN ROOM")
    page.wait_for_timeout(300)
    page.screenshot(path="/home/jules/verification/03_pin_pad_modal.png")

    # Close pin modal
    page.click("#pinPadModal .pin-modal-close")
    page.wait_for_timeout(300)

    # Click ONLINE MATCH again, then CREATE ROOM
    page.click("text=ONLINE MATCH")
    page.wait_for_timeout(300)
    page.click("text=CREATE ROOM")
    page.wait_for_timeout(300)

    # Now on Choose Exercise
    page.screenshot(path="/home/jules/verification/04_exercise_select.png")

    # Select Pushup
    page.click(".exercise-card[data-ex='pushup']")
    page.wait_for_timeout(300)

    # Now on Duration Select
    page.screenshot(path="/home/jules/verification/05_duration_select.png")

    browser.close()
    print("Verification screenshots captured successfully!")
