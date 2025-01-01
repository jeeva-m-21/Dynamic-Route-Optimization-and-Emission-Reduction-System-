import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


import tkinter as tk
from PIL import Image, ImageTk

def show_loading_screen():
    title = "Welcome to My App"
    message = "Loading... Please wait."
    image_path = r"C:\Users\jeeva\OneDrive\Documents\FedEx HAkathon\Dynamic-Route-Optimization-and-Emission-Reduction-System-\src\icon.jpg"

    def animate_spinner():
        """Creates and animates a spinning circle."""
        # Clear the canvas
        canvas.delete("all")

        # Get canvas dimensions for responsiveness
        width = canvas.winfo_width() or 200  # Default width if not yet rendered
        height = 200  # Fixed height for spinner

        # Set the size and position of the spinner
        radius = 40  # Spinner radius
        thickness = 6  # Spinner line thickness

        # Draw the spinner arc
        canvas.create_arc(
            width / 2 - radius,
            height / 2 - radius,
            width / 2 + radius,
            height / 2 + radius,  # Bounding box
            start=angle[0],
            extent=60,  # Angle of the arc
            width=thickness,  # Line thickness for smooth spinner
            outline="#FFFFFF",  # White spinner color
            style=tk.ARC,
        )

        # Update the angle to rotate the spinner
        angle[0] += 8  # Increment by smaller degrees for smooth animation

        if angle[0] >= 360:
            angle[0] = 0  # Reset the angle to start over

        # Continue the animation
        root.after(16, animate_spinner)  # Redraw every 16 ms for smooth animation

    def load_image(path, size):
        """Load and resize an image using Pillow."""
        img = Image.open(path)
        img = img.resize(size, Image.Resampling.LANCZOS)  # High-quality resizing
        return ImageTk.PhotoImage(img)

    # Create the main window
    root = tk.Tk()
    root.title(title)
    root.geometry("1920x1080")
    root.resizable(True, True)
    root.configure(bg="#000000")  # Black background

    # Top Title Label
    title_label = tk.Label(
        root,
        text=title,
        font=("Arial", 36, "bold"),
        bg="#000000",
        fg="#FFFFFF",
    )
    title_label.pack(pady=20)

    # Center Image
    if image_path:
        center_image = load_image(image_path, (300, 300))  # Resize to 300x300
        image_label = tk.Label(root, image=center_image, bg="#000000")
        image_label.pack(expand=True)

    # Bottom Message
    message_label = tk.Label(
        root,
        text=message,
        font=("Arial", 18),
        bg="#000000",
        fg="#FFFFFF",
    )
    message_label.pack(pady=10, side=tk.BOTTOM)

    # Spinner Canvas
    canvas = tk.Canvas(root, bg="#000000", bd=0, highlightthickness=0)
    canvas.pack(pady=20, side=tk.BOTTOM)

    angle = [0]  # Mutable angle to allow updates in the nested function
    animate_spinner()  # Start the spinner animation

    # Close the loading screen after 5 seconds"""
    root.after(5000, root.destroy)

    root.mainloop()

#show_loading_screen()

import tkinter as tk
from backend import noofdelivery, disttravelled, salary, fuelsaved, vehicletype, startdelivery


import tkinter as tk
from tkinter import messagebox

def save_delivery_data(address, delivery_date, vehicle_type):
    """Save the delivery data to a text file."""
    with open("deliveries.txt", "a") as file:
        file.write(f"Address: {address}\n")
        file.write(f"Delivery Date: {delivery_date}\n")
        file.write(f"Vehicle Type: {vehicle_type}\n")
        file.write("-" * 30 + "\n")
    
    # Show success message
    messagebox.showinfo("Success", "Delivery details saved successfully!")

def deliveryscreen():
    # Initialize the delivery screen window
    delivery_window = tk.Toplevel()  # Create a new top-level window
    delivery_window.title("Delivery Details")
    delivery_window.geometry("600x400")
    delivery_window.configure(bg="#1E1E1E")

    # Header Label
    header_label = tk.Label(
        delivery_window,
        text="Enter Delivery Details",
        font=("Arial", 24, "bold"),
        bg="#1E1E1E",
        fg="#FFFFFF"
    )
    header_label.pack(pady=20)

    # Create a frame for the form inputs
    form_frame = tk.Frame(delivery_window, bg="#1E1E1E")
    form_frame.pack(pady=20)

    # Address Input
    address_label = tk.Label(
        form_frame,
        text="Delivery Address:",
        font=("Arial", 14),
        bg="#1E1E1E",
        fg="#FFFFFF"
    )
    address_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
    address_entry = tk.Entry(form_frame, font=("Arial", 14), width=40)
    address_entry.grid(row=0, column=1, padx=10, pady=5)

    # Delivery Date Input
    date_label = tk.Label(
        form_frame,
        text="Delivery Date (YYYY-MM-DD):",
        font=("Arial", 14),
        bg="#1E1E1E",
        fg="#FFFFFF"
    )
    date_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
    date_entry = tk.Entry(form_frame, font=("Arial", 14), width=40)
    date_entry.grid(row=1, column=1, padx=10, pady=5)

    # Vehicle Type Input
    vehicle_label = tk.Label(
        form_frame,
        text="Vehicle Type:",
        font=("Arial", 14),
        bg="#1E1E1E",
        fg="#FFFFFF"
    )
    vehicle_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
    vehicle_entry = tk.Entry(form_frame, font=("Arial", 14), width=40)
    vehicle_entry.grid(row=2, column=1, padx=10, pady=5)

    # Submit Button to save the data
    def on_submit():
        address = address_entry.get()
        delivery_date = date_entry.get()
        vehicle_type = vehicle_entry.get()

        if not address or not delivery_date or not vehicle_type:
            messagebox.showerror("Error", "All fields are required!")
        else:
            # Save the data
            save_delivery_data(address, delivery_date, vehicle_type)
            # Close the delivery screen window
            delivery_window.destroy()

    submit_button = tk.Button(
        delivery_window,
        text="Submit Delivery",
        font=("Arial", 16),
        bg="#4CAF50",  # Green color
        fg="#FFFFFF",
        command=on_submit,
        relief="raised",
        width=20,
        height=2
    )
    submit_button.pack(pady=20)

    # Start the delivery screen window
    delivery_window.mainloop()

def main_screen():
    # Initialize the main window
    root = tk.Tk()
    root.title("Dynamic Route Optimization and Emission Reduction System")
    root.geometry("1920x1080")
    root.configure(bg="#1E1E1E")

    # Header Section
    header_frame = tk.Frame(root, bg="#2E2E2E", height=100)
    header_frame.pack(fill="x")

    # Application Title
    title_label = tk.Label(
        header_frame,
        text="Dynamic Route Optimization and Emission Reduction System",
        font=("Arial", 24, "bold"),
        bg="#2E2E2E",
        fg="#FFFFFF"
    )
    title_label.pack(pady=30)

    # Main Content Frame
    content_frame = tk.Frame(root, bg="#1E1E1E")
    content_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Left Panel for Function Values
    left_frame = tk.Frame(content_frame, bg="#1E1E1E", width=400, pady=10, padx=20)
    left_frame.pack(side="left", fill="y", expand=False)

    tk.Label(
        left_frame,
        text="Function Outputs",
        font=("Arial", 18, "bold"),
        bg="#1E1E1E",
        fg="#FFFFFF"
    ).pack(pady=10)

    # Display Values from Functions
    function_values = {
        "Number of Deliveries": noofdelivery(),
        "Distance Travelled (km)": disttravelled(),
        "Driver Salary ($)": salary(),
        "Fuel Saved (liters)": fuelsaved(),
        "Vehicle Type": vehicletype(),
        "Start Delivery Status": startdelivery(),
    }

    for name, value in function_values.items():
        tk.Label(
            left_frame,
            text=f"{name}: {value}",
            bg="#1E1E1E",
            fg="#FFFFFF",
            font=("Arial", 14),
            pady=10
        ).pack(anchor="w", padx=10)

    # Start Delivery Button
    def open_delivery_screen():
        # Call the delivery screen when the button is clicked
        deliveryscreen()

    start_button = tk.Button(
        content_frame,
        text="Start Delivery",
        font=("Arial", 16),
        bg="#4CAF50",  # Green color for the button
        fg="#FFFFFF",
        command=open_delivery_screen,  # Trigger the delivery screen
        relief="raised",
        width=20,
        height=2
    )
    start_button.pack(pady=20)

    # Footer Section
    footer_frame = tk.Frame(root, bg="#2E2E2E", height=50)
    footer_frame.pack(fill="x", side="bottom")

    footer_label = tk.Label(
        footer_frame,
        text="© 2024 Dynamic Route Optimization. All Rights Reserved.",
        font=("Arial", 12),
        bg="#2E2E2E",
        fg="#FFFFFF"
    )
    footer_label.pack(pady=10)

    # Start the main loop
    root.mainloop()

# Call the function to display the main screen
if __name__ == "__main__":
    main_screen()