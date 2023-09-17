import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def analyze_data():
    """
    Generate 100 random data points and compute their mean and standard deviation.
    """
    data = np.random.randn(100)
    mean = np.mean(data)
    std_dev = np.std(data)
    return data, mean, std_dev

def main():
    st.set_page_config(page_title='Data Analysis App', layout='wide')
    st.title("Random Data Analysis")
    
    data, mean, std_dev = analyze_data()

    st.write(f"Mean: {mean:.2f}")
    st.write(f"Standard Deviation: {std_dev:.2f}")

    fig, ax = plt.subplots()
    ax.hist(data, bins=20, alpha=0.6, color='b')
    st.pyplot(fig)

if __name__ == '__main__':
    main()
