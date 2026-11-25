<div align="center">

<img src="https://img.shields.io/badge/STOVEST-Explore%20Markets.%20Understand%20Trends.%20Build%20Insights.-101B33?style=for-the-badge&labelColor=2457D6" alt="Stovest Banner" />

<br /><br />

# STOVEST

### *Explore Markets. Understand Trends. Build Insights.*

**Making stock market exploration simple, visual and accessible.**

A friendly way to save the companies you follow, look up their historical stock prices, and see how they have moved over time on a clean chart.

<br />

[![GitHub Stars](https://img.shields.io/github/stars/DhineshkarthikR/stovest?style=for-the-badge&color=16A36A&labelColor=101B33&logo=github)](https://github.com/DhineshkarthikR/stovest/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/DhineshkarthikR/stovest?style=for-the-badge&color=2457D6&labelColor=101B33&logo=github)](https://github.com/DhineshkarthikR/stovest/network/members)
[![Open Issues](https://img.shields.io/github/issues/DhineshkarthikR/stovest?style=for-the-badge&color=2457D6&labelColor=101B33&logo=github)](https://github.com/DhineshkarthikR/stovest/issues)
[![MIT License](https://img.shields.io/github/license/DhineshkarthikR/stovest?style=for-the-badge&color=16A36A&labelColor=101B33)](LICENSE)

<br />

[See How It Works](#-see-how-it-works) &nbsp;•&nbsp; [Application Preview](#-application-preview) &nbsp;•&nbsp; [Get Started](#-getting-started) &nbsp;•&nbsp; [Join the Journey](#-join-the-journey)

</div>

---

## 💡 The Idea Behind Stovest

Have you ever wondered how the price of your favourite company's stock has changed over time?

For most people, looking up stock prices feels overwhelming. Financial websites are packed with cluttered charts, unfamiliar numbers, and confusing jargon before you even get a simple answer to a simple question: *Did this stock go up or down over the last few weeks?*

**Stovest** was created to make that first step effortless. Instead of drowning you in complex trading screens, it gives you a quiet, focused space to keep a personal list of companies, pick any time window you are curious about, and see the story of a stock's historical price movement through a clear visual chart.

---

## ✨ What Can You Do With Stovest?

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>📌 Save Your Stocks</h3>
      <p>Keep your own list of company names and stock symbols (like <code>AAPL</code> or <code>TCS.NS</code>) so you do not have to look them up every time.</p>
    </td>
    <td width="50%" valign="top">
      <h3>🔍 Explore Stock Prices</h3>
      <p>Type in a stock symbol and choose how many days of historical market data you want to examine—whether that is a week, a month, or longer.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>📈 Visualize Market Movement</h3>
      <p>See historical <strong>closing prices</strong> (the final price of a stock at the end of each trading day) plotted on an easy-to-read line chart.</p>
    </td>
    <td width="50%" valign="top">
      <h3>🧭 Understand Price Direction</h3>
      <p>Automatically compare the starting and ending closing prices in your chosen period to see whether the overall movement was upward or downward.</p>
    </td>
  </tr>
</table>

---

## 🚀 See How It Works

Exploring a stock with Stovest takes four simple steps:

1. **Add a company and its stock symbol** — Build your personal list by entering a company name and its market ticker (for example, `TCS.NS` or `AAPL`).
2. **View your saved stock list** — Check the companies you have stored whenever you want a quick reminder of their symbols.
3. **Select a stock and an analysis period** — Pick a company symbol and decide how many past days of prices you would like to inspect.
4. **Explore the resulting price chart and historical movement** — A visual line chart opens showing the daily closing prices, followed by a quick summary comparing the first day to the last day.

---

## 🖥️ Application Preview

Stovest runs directly in your terminal and opens an interactive **Matplotlib** chart window whenever you analyze a stock.

When you launch the app, you are greeted with a simple three-option menu:

```text
1. CREATE TABLE OF TICKER SYMBOL.
2. DISPLAY TICKER SYMBOL.
3. ANALYZE THE STOCK.
Enter your choice:
```

Choosing **Option 3** fetches historical daily data for your chosen number of days, displays a line chart of closing prices, and prints a simple start-to-end comparison in the terminal.

<!-- Add genuine application & chart screenshots here when available -->

---

## 👥 Who Is Stovest For?

- **Students exploring the stock market** who want a hands-on way to see how company stock prices move over time.
- **Beginners learning about historical stock prices** without needing to navigate intimidating financial terminals.
- **Finance enthusiasts** who are curious about checking short- and medium-term price movements for companies they follow.
- **Developers** interested in exploring a clean, straightforward example of stock market analysis and financial data visualization in Python.

---

## 🔧 Behind the Scenes

<details>
<summary><strong>Curious about how Stovest works?</strong> (Click to expand)</summary>

<br />

Under the hood, Stovest connects four straightforward tools:

- **Python** powers the terminal menu, user prompts, and overall application flow.
- **MySQL** stores your saved list of company names and stock ticker symbols in a local database.
- **Yahoo Finance (`yfinance`)** provides historical daily stock price data for the ticker and number of days you request *(note: Stovest looks up historical data rather than live real-time streaming prices)*.
- **Matplotlib** draws the closing price line chart in a dedicated window so you can visually inspect the trend.

</details>

---

## 🛠️ Getting Started

Want to try Stovest on your own computer? You will need **Python** and a local **MySQL** server.

<details>
<summary><strong>Step-by-step setup instructions</strong> (Click to expand)</summary>

<br />

### 1. Download the Project

```bash
git clone https://github.com/DhineshkarthikR/stovest.git
cd stovest
```

### 2. Set Up a Python Virtual Environment

Create and activate an isolated environment for the project:

```bash
python -m venv venv
```

**On Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**On macOS / Linux:**

```bash
source venv/bin/activate
```

### 3. Install Required Packages

```bash
pip install yfinance matplotlib mysql-connector-python
```

### 4. Set Up the MySQL Database

Open your MySQL client and create the database that Stovest uses to store your stock list:

```sql
CREATE DATABASE stock_market;
```

Before running the app, open `STOCK MARKET INVETSMENT ADVISOR.py` and make sure the MySQL connection settings (`host`, `user`, `password`, and `database`) match your local MySQL server configuration.

### 5. Run Stovest

```bash
python "STOCK MARKET INVETSMENT ADVISOR.py"
```

</details>

---

## 🗺️ What's Coming Next?

Stovest is an evolving project. The ideas below are **future plans**—they are not yet implemented in the current version:

- [ ] **Multiple stock comparison** — Compare price movements of two or more companies on the same chart.
- [ ] **Technical indicators** — Add popular trend helpers like moving averages to spot patterns more easily.
- [ ] **Better watchlist management** — Edit, search, and remove saved stocks directly from the menu.
- [ ] **Portfolio tracking** — Keep track of hypothetical or personal holdings over time.
- [ ] **Visual dashboard** — Provide a dedicated graphical interface alongside the terminal experience.
- [ ] **Exportable analysis reports** — Save charts and price summaries for offline reading.

---

## 🤝 Join the Journey

Stovest is open source and built for learning. If you find the idea interesting, you are welcome to explore and get involved:

- ⭐ **Star the repository** on [GitHub](https://github.com/DhineshkarthikR/stovest) if you would like to bookmark or support the project.
- 🍴 **Fork the project** to experiment with your own ideas.
- 🐛 **Report bugs or suggest improvements** by opening an issue on the [Issue Tracker](https://github.com/DhineshkarthikR/stovest/issues).

---

## ⚠️ Disclaimer

Stovest is an **educational project** created to help users explore historical stock market data and charts.

The application uses historical data from Yahoo Finance (not real-time streaming quotes) and checks price direction simply by comparing the first and last closing prices in the selected time period. While the terminal output prints simple labels such as *"Safe to Invest!"* or *"Risky to Invest!"* based on that start-to-end comparison, **this is a basic historical observation—not investment advice**, and it cannot determine whether any stock is safe to buy. Always do your own research or consult a qualified financial advisor before making financial decisions.

---

<div align="center">

### Built with curiosity by [Dhinesh Karthik R](https://github.com/DhineshkarthikR).

*Explore Markets. Understand Trends. Build Insights.*

Licensed under the [MIT License](LICENSE).

</div>
