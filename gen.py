def page(number: int):
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Thai Grad 2024: Graduation Photos</title>
<style>
  .navigation-container {'{'}
    display: flex;
    justify-content: center;
    margin-top: 20px;
  {'}'}
  .p-btn, .n-btn {'{'}
    padding: 10px 20px;
    margin: 0 10px;
    font-size: 16px;
    cursor: pointer;
  {'}'}
  img {'{'}
    margin: 10px;
  {'}'}
</style>
</head>
<body>
  <div class="navigation-container">
    <a href="http://chanwutk.github.io/2024-04-21-grad-photos/{(number-1):02d}" class="p-btn">prev</a>
    <a href="http://chanwutk.github.io/2024-04-21-grad-photos/{(number+1):02d}" class="n-btn">next</a>
  </div>
  <div style="display: flex; flex-direction: row; flex-wrap: wrap;">
    <a href="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/DSCF0{number:02d}0.JPG?raw=true"><img src="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/SMALL-DSCF0{number:02d}0.JPG?raw=true" alt="" width="45%" height="auto"></a>
    <a href="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/DSCF0{number:02d}1.JPG?raw=true"><img src="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/SMALL-DSCF0{number:02d}1.JPG?raw=true" alt="" width="45%" height="auto"></a>
    <a href="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/DSCF0{number:02d}2.JPG?raw=true"><img src="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/SMALL-DSCF0{number:02d}2.JPG?raw=true" alt="" width="45%" height="auto"></a>
    <a href="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/DSCF0{number:02d}3.JPG?raw=true"><img src="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/SMALL-DSCF0{number:02d}3.JPG?raw=true" alt="" width="45%" height="auto"></a>
    <a href="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/DSCF0{number:02d}4.JPG?raw=true"><img src="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/SMALL-DSCF0{number:02d}4.JPG?raw=true" alt="" width="45%" height="auto"></a>
    <a href="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/DSCF0{number:02d}5.JPG?raw=true"><img src="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/SMALL-DSCF0{number:02d}5.JPG?raw=true" alt="" width="45%" height="auto"></a>
    <a href="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/DSCF0{number:02d}6.JPG?raw=true"><img src="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/SMALL-DSCF0{number:02d}6.JPG?raw=true" alt="" width="45%" height="auto"></a>
    <a href="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/DSCF0{number:02d}7.JPG?raw=true"><img src="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/SMALL-DSCF0{number:02d}7.JPG?raw=true" alt="" width="45%" height="auto"></a>
    <a href="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/DSCF0{number:02d}8.JPG?raw=true"><img src="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/SMALL-DSCF0{number:02d}8.JPG?raw=true" alt="" width="45%" height="auto"></a>
    <a href="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/DSCF0{number:02d}9.JPG?raw=true"><img src="https://github.com/chanwutk/2024-04-21-grad-photos/blob/main/SMALL-DSCF0{number:02d}9.JPG?raw=true" alt="" width="45%" height="auto"></a>
  </div>
  <div class="navigation-container">
    <a href="http://chanwutk.github.io/2024-04-21-grad-photos/{(number-1):02d}" class="p-btn">prev</a>
    <a href="http://chanwutk.github.io/2024-04-21-grad-photos/{(number+1):02d}" class="n-btn">next</a>
  </div>
</body>
</html>
"""

for i in range(19):
    with open(f"./site/{i:02d}.html", "w") as f:
        f.write(page(i))