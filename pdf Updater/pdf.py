import subprocess

class main:
    @staticmethod
    def convert_docx_to_pdf(input_file, output_dir):
        try:
            # Command to convert the document
            command = [
                "/usr/lib/libreoffice/program/soffice",  # Path to LibreOffice executable
                "--headless",
                "--convert-to", "pdf",
                "--outdir", output_dir,
                input_file
            ]

            # Run the command
            subprocess.run(command, check=True)
            print(f"Conversion completed: {input_file} -> {output_dir}")

        except subprocess.CalledProcessError as e:
            print(f"An error occurred during conversion: {e}")

    # if __name__ == "__main__":
    #     # input_file = "/workspaces/Document_Updater/Updated/NDA_Dha.docx"
    #     # output_dir = "/workspaces/Document_Updater/Updated/PDF/NDA_Dha.docx"
    #     convert_docx_to_pdf(input_file, output_dir)
