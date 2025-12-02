import streamlit as st
import json
import os

CONTACTS_FILE = "contacts.json"
# project made by Harrison Nordmeyer, Cuyler Zukowski, Daniel You
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

st.sidebar.markdown("---")
st.sidebar.header("⚙️ Data Options")

json_string = json.dumps(contacts, indent=4)

st.sidebar.download_button(
    label="📥 Backup Contacts",
    file_name="contacts_backup.json",
    mime="application/json",
    data=json_string
)



# --- View Contacts ---
if menu == "View Contacts":
    st.header("All Contacts")
    if not contacts:
        st.info("No contacts found.")
    else:
        for name, info in contacts.items():
            st.write(f"**{name}**")
            st.write(f"🏷️ {info.get('category', 'Other')}")
            st.write(f"📞 {info.get('phone', '')}")
            st.write(f"📧 {info.get('email', '')}")
            st.write(f"🏠 {info.get('address', '')}")
            st.write(f"📝 {info.get('notes', '')}")
            st.divider()

# --- Add Contact ---
elif menu == "Add Contact":
    st.header("Add New Contact")
    name = st.text_input("Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")
    address = st.text_area("Address")
    notes = st.text_area("Notes")

    category = st.selectbox("Category", ["Family", "Friend", "Work", "School", "Other"])

    if st.button("Add Contact"):
        if name in contacts:
            st.error("Contact already exists.")
        else:
            contacts[name] = {"phone": phone, "email": email, "address": address, "notes": notes, "category": category}
            save_contacts(contacts)
            st.success(f"{name} added successfully!")


# --- Search Contact --- ~(Updated field to handle case sensitivity, partial matches, and can search all fields)
elif menu == "Search Contact":
    st.header("Search Contact")
    search_term = st.text_input("Enter search term").lower()
    found_contacts = False

    if st.button("Search"):
        for name, info in contacts.items():

            phone = info.get('phone', '')
            email = info.get('email', '')
            address = info.get('address', '')
            notes = info.get('notes', '')


            if (search_term in name.lower() or 
                search_term in phone.lower() or 
                search_term in email.lower() or
                search_term in address.lower() or 
                search_term in notes.lower()):

                
                st.success(f"**{name}** found!")
                st.write(f"📞 {info['phone']}")
                st.write(f"📧 {info['email']}")
                st.divider()
                found_contacts = True

        if not found_contacts:
            st.error("No contacts found matching that term.")




# --- Update Contact ---
elif menu == "Update Contact":
    st.header("Update Contact")
    name = st.text_input("Enter name to update")
    if name in contacts:
        new_phone = st.text_input("New Phone Number", value=contacts[name].get('phone', ''))
        new_email = st.text_input("New Email", value=contacts[name].get('email', ''))
        new_address = st.text_area("Address", value=contacts[name].get('address', ''))
        new_notes = st.text_area("Notes", value=contacts[name].get('notes', ''))
    

        current_category = contacts[name].get('category', 'Other')
        category_options = ["Family", "Friend", "Work", "School", "Other"]
        
        try:
            index = category_options.index(current_category)
        except ValueError:
            index = 4 

        new_category = st.selectbox("Category", category_options, index=index)

        if st.button("Update Contact"):
            contacts[name]["phone"] = new_phone
            contacts[name]["email"] = new_email
            contacts[name]["address"] = new_address
            contacts[name]["notes"] = new_notes
            contacts[name]["category"] = new_category
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
