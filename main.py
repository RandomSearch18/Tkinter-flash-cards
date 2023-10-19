from tkinter import *
from tkinter import ttk, font


# Test edit

class Flashcard:

    def __init__(self, label: str, content: str):
        self.label = label
        self.content = content.strip()

    def activate(self, target_widget: Text):
        """Writes the flashcard's content to the target widget"""
        # Text can't be edited when disabled, so we have to set it to normal and back again
        target_widget.config(state="normal")
        # Replace all existing content (0.0 to the end) with our content
        target_widget.replace("0.0", END, self.content)
        target_widget.config(state="disabled")

    def place_button(self, parent: Frame, flashcard_target: Text):
        """Creates a button that can be clicked to show the flashcard content

        - Expects the parent frame to be a single column of other buttons
        - Places the new button at the bottom of the frame
        - flashcard_target= specifies the Text widget that the flashcard contents will be written to
        """
        button = ttk.Button(
            parent,
            command=lambda: self.activate(flashcard_target),
            text=self.label,
            width=15,
        )

        # Place the button at the bottom
        num_children = len(parent.children)
        button.grid(row=num_children, pady=(5, 0))


def scale_default_font(factor: float):
    """Returns the default system font, with its size increased by a scale factor"""
    our_font = font.nametofont("TkDefaultFont").copy()
    original_size = our_font.cget("size")
    modified_size = int(original_size * factor)
    our_font.config(size=modified_size)
    return our_font


def draw_main_text() -> Text:
    """Adds the text widget that contains flashcard data to the UI"""
    initial_content = (
        "Welcome to the computing hardware flashcards program!\n\n" +
        "Click one of the buttons to the left, or use the Tab and Space keys, to select a topic."
    )
    widget = Text(
        body,
        height=20,
        width=60,
        borderwidth=0,
        wrap="word",
        font=scale_default_font(1.3),
    )
    widget.insert(1.0, initial_content)
    widget.config(state="disabled")
    widget.grid(
        column=1,
        row=0,
    )
    return widget


def draw_flashcard_buttons(flashcards: list) -> Frame:
    """Adds the buttons for activating flashcards to the UI"""
    # Create a frame to place the flashcard buttons in
    buttons_frame = ttk.Frame(body)
    buttons_frame.grid(
        column=0,
        row=0,
        # Add padding to the right to create a gap between the main text and the buttons
        padx=(0, 10),
    )

    for flashcard in flashcards:
        flashcard.place_button(buttons_frame, flashcard_target=main_text)

    return buttons_frame


# Initialise Tkinter window and a frame for the main UI
window = Tk()
window.title("Flash Cards - Computing Hardware")
body = ttk.Frame(window, padding=10)
body.grid()

# Use the more modern Clam theme for tk widgets
style = ttk.Style()
style.theme_use("clam")

# Define the flashcards
flashcards = [
    Flashcard(
        "The CPU",
        """
The CPU (central processing unit) is one of the most important computer components, performing most of the processing tasks in a computer system.

Modern CPU clock speeds range from around 0.1 GHz (embedded systems), to 2 GHz (mobile phones) and up to 5 GHz (high-end desktops). \
In addition, while embedded systems tend to have 1 or 2 cores, desktop CPUs benefit from 4 to 16 cores, to provide smoother multitasking.

The CPU is the primary heat source in a computer system, with its heat generation quantified by its TDP (Thermal Design Power) rating. \
High-end desktop CPUs can produce well over 100W of heat, while lower-performance CPUs typically generate around 50W for desktops, 15W for laptops, or down to 5W for mobile devices. \
This demonstrates the diversity in CPU design, adapting to a range of uses, with the appropriate comprise between performance and power/cooling demands.
        """,
    ),
    Flashcard(
        "RAM",
        """
RAM (random-access memory) is used to store the programs that are currently running on the system, as well as any data being accessed by those programs. \
RAM is non-persistent, so it is cleared when the computer loses power.

It can also be used as cache to speed up opening programs, as accessing RAM is about 100x faster than an SSD (but 100x slower than CPU cache).

Servers that need low-latency, high-performance access to databases often use RAM to store all or parts of the database to provide real-time access.
        """,
    ),
    Flashcard(
        "I/O devices",
        """
I/O (input/output) devices bridge the gap between the computer's hardware and the user (or other systems) by letting them receive output and send input to the system.

Input devices include keyboards, pointing devices (mice/touchscreens), microphones, webcams, and sensors like accelerometers.

Output devices include monitors and built-in displays, speakers, printers, and status LEDs.

While most I/O devices are used for direct user interaction, some of them (like network interfaces and storage devices) are for interacting with other systems or devices. \
These are an important part of "headless" systems, such as servers.
        """,
    ),
    Flashcard(
        "Storage devices",
        """
Storage devices provide a way to persistently store data in computer systems. They are most commonly used as secondary storage, but tertiary storage also exists, used for long-term data archival.

Storage capacities for desktops start at 800 MB (CDs), and go up to 8 TB (SSDs) or 20 TB (hard drives).

While hard drives used to be the predominant storage technology, SSD prices have fallen rapidly in recent years, and many desktops today come with 1 or 2 TB of solid-state storage.

Modern mobiles tend to use UFS (universal flash storage), a higher-performance successor to eMMC (embedded MultiMediaCard), usually with hundreds of GB of capacity.

Microcontrollers and other embedded systems usually have a few MB of flash storage to store program data.
        """,
    ),
    Flashcard(
        "Motherboard",
        """
The motherboard is a PCB (printed circuit board) and serves as the physical base for components in a desktop computer, providing power, electronic connections, and physical mounts.

Connectors found on motherboards include CPU sockets, RAM slots, PCIe slots, and external connectors like USB ports and audio jacks.

The motherboard also contains a ROM chip with UEFI (Unified Extensible Firmware Interface) firmware to handle boot-up and low-level hardware initialisation.
    """,
    ),
]

# Draw the UI elements
main_text = draw_main_text()
flashcard_buttons = draw_flashcard_buttons(flashcards)

# Show the window and begin the main loop
window.mainloop()
