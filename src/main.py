

import tkinter as tk
from backend import noofdelivery, disttravelled, salary, fuelsaved, vehicletype, startdelivery


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

    # Left Panel for Function Values
    left_frame = tk.Frame(root, bg="#1E1E1E", width=400, pady=10, padx=20)
    left_frame.pack(side="left", fill="y")

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
        "Distance Travelled": disttravelled(),
        "Driver Salary": salary(),
        "Fuel Saved": fuelsaved(),
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

    # Right Panel for Details
    right_frame = tk.Frame(root, bg="#1E1E1E", pady=20, padx=20)
    right_frame.pack(side="right", expand=True, fill="both")

    tk.Label(
        right_frame,
        text="Real-Time Data (Placeholder)",
        font=("Arial", 18, "bold"),
        bg="#1E1E1E",
        fg="#FFFFFF"
    ).pack(pady=10)

    # Placeholder for real-time data
    traffic_label = tk.Label(
        right_frame,
        text="Traffic Status: Loading...",
        font=("Arial", 14),
        bg="#1E1E1E",
        fg="#FFFFFF"
    )
    traffic_label.pack(pady=5)

    weather_label = tk.Label(
        right_frame,
        text="Weather Info: Loading...",
        font=("Arial", 14),
        bg="#1E1E1E",
        fg="#FFFFFF"
    )
    weather_label.pack(pady=5)

    # Footer Section
    footer_frame = tk.Frame(root, bg="#2E2E2E", height=50)
    footer_frame.pack(fill="x")

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
