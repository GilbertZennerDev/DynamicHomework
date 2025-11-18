# DynamicHomework
## ✨ What is the Homework Dynamo?

Tired of static, boring assignment lists? **The Homework Dynamo is the answer\!**

This sleek Python project, built with the power of Streamlit, **dynamically** and **randomly** generates a defined number of tasks from various subjects and difficulty levels. It is the ultimate proof of how simple and effective modern Python tools can be used to solve everyday problems.

**The Goal:** Never see the same assignments again\! Provide students with an **infinite source** of variable exercises.

-----

## 🎯 Core Features (The Punchlines)

  * **⚡️ Load Once (Smart Caching):** Thanks to **clever Streamlit Session State**, the costly disk read operation is executed only **a single time** on the first run. **Maximize performance, minimize wait time\!**
  * **🛠️ Dynamic Control:** Select the Subject (German, English, Math, etc.), the Level (1-10), and the exact **Amount** of tasks using intuitive sliders and dropdowns.
  * **🎲 True Randomness:** The `XTasks` function **guarantees** a random selection of assignments, preventing repetition (as long as enough tasks are available).
  * **🧑‍💻 Clean Architecture:** Clearly defined classes (`Student`) and modular functions (`CleanTasks`, `ReadSubjectFile`) make the code **readable, maintainable**, and **extensible**.

-----

## 🚀 Installation & Launch

You will need Python 3.x and Streamlit.

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
    cd YOUR_REPO_NAME
    ```

2.  **Install Dependencies:**

    ```bash
    pip install streamlit
    ```

3.  **Set Up Data Structure:**
    Ensure you have the `subjects` folder with subfolders for your subjects and the corresponding `.txt` files for the levels (e.g., `subjects/german/german_level1.txt`).

4.  **Run the App:**

    ```bash
    streamlit run YOUR_MAIN_FILENAME.py
    ```

    *(Replace `YOUR_MAIN_FILENAME.py` with the actual name of your Python file, e.g., `app.py` or `generator.py`)*

-----

## 💡 How It Works (Usage)

Once started, the Streamlit app will open in your browser.

1.  Enter your name (for a friendly welcome\!).
2.  Select the **Subject** from the dropdown.
3.  Define the **Level** (1-10) using the slider.
4.  Choose the **desired Amount** of assignments (1-30).

**Result:** The app instantly displays your **freshly generated, random** tasks\!

-----

## 🛠️ Technology Stack

  * **Python:** The foundation for all the core logic.
  * **Streamlit:** Enables building a **beautiful, interactive** web application with minimal effort.
  * **Random:** Used for the fair and unpredictable selection of homework tasks.

-----

## 🤝 Contributing

This project proves how much power a small Python script can hold. Do you have ideas on how to make the generator even better (e.g., task upload feature, expanded subjects)?

1.  Fork the Repository.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

-----

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

-----

> **Built with 🖤 and Python 🐍 by [GilbertZennerDev]**# DynamicTeaching
