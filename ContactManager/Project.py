import streamlit as st
import json
import os

CONTACTS_FILE = "contacts.json"

# --- Helper Functions ---
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# --- Streamlit App ---
st.set_page_config(page_title="Contact Book", page_icon="📒", layout="centered")
st.title("📒 Contact Book")

# Load contacts
contacts = load_contacts()

# Sidebar Navigation
menu = st.sidebar.radio("Menu", ["View Contacts", "Add Contact", "Search Contact", "Update Contact", "Delete Contact"])

# --- View Contacts ---
if menu == "View Contacts":
    st.header("All Contacts")
    if not contacts:
        st.info("No contacts found.")
    else:
        for name, info in contacts.items():
            st.write(f"**{name}**")
            st.write(f"📞 {info['phone']}")
            st.write(f"📧 {info['email']}")
            st.divider()

# --- Add Contact ---
elif menu == "Add Contact":
    st.header("Add New Contact")
    name = st.text_input("Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")

    if st.button("Add Contact"):
        if name in contacts:
            st.error("Contact already exists.")
        else:
            contacts[name] = {"phone": phone, "email": email}
            save_contacts(contacts)
            st.success(f"{name} added successfully!")

# --- Search Contact ---
elif menu == "Search Contact":
    st.header("Search Contact")
    search_name = st.text_input("Enter name to search")
    if st.button("Search"):
        if search_name in contacts:
            st.success(f"**{search_name}** found!")
            st.write(f"📞 {contacts[search_name]['phone']}")
            st.write(f"📧 {contacts[search_name]['email']}")
        else:
            st.error("Contact not found.")

# --- Update Contact ---
elif menu == "Update Contact":
    st.header("Update Contact")
    name = st.text_input("Enter name to update")
    if name in contacts:
        new_phone = st.text_input("New Phone Number", value=contacts[name]["phone"])
        new_email = st.text_input("New Email", value=contacts[name]["email"])
        if st.button("Update Contact"):
            contacts[name]["phone"] = new_phone
            contacts[name]["email"] = new_email
            save_contacts(contacts)
            st.success(f"{name} updated successfully!")
    elif name:
        st.error("Contact not found.")

# --- Delete Contact ---
elif menu == "Delete Contact":
    st.header("Delete Contact")
    name = st.text_input("Enter name to delete")
    if st.button("Delete"):
        if name in contacts:
            del contacts[name]
            save_contacts(contacts)
            st.success(f"{name} deleted successfully!")
        else:
            st.error("Contact not found.")
