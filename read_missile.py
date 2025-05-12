def extract_selected_features(file_path):
    keywords = ["range", "speed", "warhead", "guidance", "mobility"]
    extracted_lines = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                lower_line = line.lower()
                if any(keyword in lower_line for keyword in keywords):
                    extracted_lines.append(line.strip())

        if not extracted_lines:
            return "No matching technical features found."
        return "\n".join(extracted_lines)

    except FileNotFoundError:
        return "File not found. Please check the path and filename."

# Example usage
file_path = "MISSILE.txt"
features = extract_selected_features(file_path)
print("Selected Technical Features:\n")
print(features)

