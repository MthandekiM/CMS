class CMS:

    def __init__(self):
        self.contents = []

    # Defining method to add content
    def add_content(self):
        title = input("Enter the title of the content")
        body = input("Enter the body of the content")

        self.contents.append({"title": title, "body": body})

        print("Content added successfully!")


    # Defining method to view content
    def view_content(self):
        if not self.contents:
            print("No content available!")
            return

        for idx, content in enumerate(self.contents, start=1):
            print(f"\nContent {idx}")
            print(f"Title: {content['title']}")
            print(f"Body: {content['body']}")


    # Defining method to edit content
    def edit_content(self):
        self.view_content()

        if not self.contents:
            return

        content_id = int(input("Enter the number of the content you want to edit: ")) - 1

        if 0 <= content_id < len(self.contents):
            title = input("Enter the new title: ")
            body = input("Enter the new body: ")
            self.contents[content_id] = {"title": title, "body": body}
            print("Content updated successfully!")

        else:
            print("Invalid content number!")


    # Defining method to delete content
    def delete_content(self):
        self.view_content()

        if not self.contents:
            return

        content_id = int(input("Enter the number of the content you want to delete: ")) - 1

        if 0 <= content_id < len(self.contents):
            del self.contents[content_id]
            print("Content deleted successfully!")

        else:
            print("Invalid content number!")

    # Running the CMS
    def run(self):
        while True:

            print("\nCMS Menu:")
            print("1. Add Content")
            print("2. View Content")
            print("3. Edit Content")
            print("4. Delete Content")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_content()
            elif choice == "2":
                self.view_content()
            elif choice == "3":
                self.edit_content()
            elif choice == "4":
                self.delete_content()
            elif choice == "5":
                print("Exiting the CMS...")
                break
            else:
                print("Invalid choice! Please try again.")


if __name__ == "__main__":
    cms = CMS()
    cms.run()
