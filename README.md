# 🛡️ SentinelAI

**SentinelAI** is an AI-based disinformation intelligence system designed to detect
coordinated misinformation narratives using sentiment analysis, narrative repetition,
and behavioral signals — without targeting individuals.



##  Architecture

![Sentinel AI Architecture](data/sentinel-ai-architecture.jpeg)




## 🚀 Features
- Sentiment & emotion analysis
- Narrative repetition detection
- Sentiment spike detection
- Explainable disinformation risk score
- Human-in-the-loop dashboard
- Privacy-first and ethical AI design



## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd SENTINELAI
   ```

2. **Create virtual environment**
   ```bash
   python -m venv myenv
   # Windows
   myenv\Scripts\activate
   # macOS/Linux
   source myenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r backend/requirements.txt
   pip install -r dashboard/requirements.txt
   ```

---

## 🏃‍♂️ Running the System

### 1. Start the Backend API
```bash
cd backend
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

### 2. Start the Dashboard
```bash
cd dashboard
streamlit run app.py
```

The dashboard will open at `http://localhost:8501`.

---

## 📊 How It Works

### Input Processing
1. User enters social media posts
2. Backend cleans and preprocesses text
3. Sentiment and emotion analysis performed

### Disinformation Detection
1. **Sentiment Spike Detection**: Detects sudden increases in negative sentiment
2. **Narrative Repetition**: Identifies repeated phrases and themes
3. **Behavioral Signals**: Detects coordinated patterns (in future versions)

### Risk Assessment
- **Risk Score**: 0-100 (higher = more risk)
- **Threat Level**: Low / Medium / High / Critical
- **Explainability**: Shows contributing factors for each risk

---

## ⚖️ Ethical Considerations

SentinelAI is built on ethical AI principles:

- ✅ Analyzes only **publicly available text**
- ✅ Does **not collect or store personal identities**
- ✅ Focuses on **narratives and patterns**, not individuals
- ✅ Provides **risk indicators**, not automated decisions
- ✅ Requires **human interpretation** for all high-risk outputs

This system is designed to **support informed decision-making**, not censorship or surveillance.

---

## 📁 Project Structure

```
SENTINELAI/
├── backend/                 # FastAPI backend
│   ├── main.py              # API entry point
│   ├── sentiment.py         # Sentiment & emotion analysis
│   ├── narrative.py         # Narrative detection
│   ├── risk.py              # Risk assessment
│   ├── utils.py             # Utility functions
│   └── requirements.txt     # Backend dependencies
│
├── dashboard/               # Streamlit dashboard
│   ├── app.py               # Main dashboard application
│   └── requirements.txt     # Dashboard dependencies
│
├── data/                    # Sample data (optional)
│   └── sample_posts.csv
│
├── .gitignore               # Git ignore file
└── README.md                # Project documentation
