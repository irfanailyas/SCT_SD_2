import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", layout="centered")

# Initialize session state variables
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.hint_shown = False

st.title("🎯 Number Guessing Game")
st.markdown("Guess a number between **1 and 100**. You have **7 attempts**.")

# Game logic
if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1

        if guess == st.session_state.number:
            st.success(f"🎉 Correct! You guessed the number in {st.session_state.attempts} attempt(s).")
            st.session_state.game_over = True
        elif guess < st.session_state.number:
            st.warning("Too low. Try again.")
        else:
            st.warning("Too high. Try again.")

        if st.session_state.attempts >= 7 and not st.session_state.game_over:
            st.error(f"❌ Game Over! The correct number was {st.session_state.number}.")
            st.session_state.game_over = True

        # Show a hint after 3 wrong attempts
        if st.session_state.attempts == 3 and not st.session_state.hint_shown:
            hint = "even" if st.session_state.number % 2 == 0 else "odd"
            st.info(f"Hint: The number is {hint}.")
            st.session_state.hint_shown = True

# Restart the game
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.hint_shown = False
