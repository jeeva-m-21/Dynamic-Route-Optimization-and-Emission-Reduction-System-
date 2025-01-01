'''def show_loading_screen():
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

    # Close the loading screen after 5 seconds
    root.after(5000, root.destroy)

    root.mainloop()
'''