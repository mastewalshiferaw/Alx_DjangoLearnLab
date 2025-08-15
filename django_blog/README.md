### How the Comment System Works

The system allows for full Create, Read, Update, and Delete (CRUD) operations on comments associated with blog posts.

-   **Create:** Logged-in users can add new comments to any blog post.
-   **Read:** All visitors (logged-in or not) can see the comments section below each post.
-   **Update:** Users can edit their own comments after they have been posted.
-   **Delete:** Users can delete their own comments.

### User Permissions & Rules

Permissions are strictly enforced to ensure users can only manage their own content.

1.  **Adding Comments:**
    -   **Rule:** Only authenticated (logged-in) users can add a comment.
    -   **Implementation:** The UI displays an "Add Comment" button for logged-in users, which links to a separate creation page (`/post/<id>/comments/new/`). For logged-out users, it displays a "Please log in to comment" message.

2.  **Editing and Deleting Comments:**
    -   **Rule:** A user can ONLY edit or delete their OWN comments. They cannot affect comments made by other users.
    -   **Implementation:**
        -   The system uses Django's `UserPassesTestMixin` in the `CommentUpdateView` and `CommentDeleteView` to check if `request.user == comment.author`.
        -   If the check fails, the user receives a "403 Forbidden" error, preventing unauthorized access.
        -   The user interface (UI) on the post detail page also checks `if comment.author == user` and only shows the "Edit" and "Delete" buttons next to the comments that belong to the current user.

### How to Test the Comment Features

1.  **Test Adding a Comment:**
    -   Log in to an account.
    -   Navigate to any post's detail page.
    -   Click the "Add Comment" button.
    -   Fill out the form and click "Submit."
    -   **Expected Result:** You should be redirected back to the post detail page, and your new comment should appear in the comments section with a success message.

2.  **Test Editing a Comment:**
    -   As the same user, find the comment you just created.
    -   Click the "Edit" link next to it.
    -   Change the text in the form and click "Update."
    -   **Expected Result:** You should be redirected back to the post detail page, and your comment should show the updated text.

3.  **Test Permissions (Unauthorized Edit):**
    -   Log out and log in with a *different* user account.
    -   Navigate to the same post.
    -   **Expected Result:** You should see the first user's comment, but there should be **no** "Edit" or "Delete" links next to it. Manually trying to go to the edit URL (`/comment/<id>/update/`) should result in a 403 Forbidden error page.

4.  **Test Deleting a Comment:**
    -   Log back in as the original author of the comment.
    -   Click the "Delete" link next to your comment.
    -   On the confirmation page, click "Yes, Delete."
    -   **Expected Result:** You should be redirected back to the post detail page, and your comment should be gone.