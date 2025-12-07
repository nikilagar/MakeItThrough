# Privacy Policy for TruthLens

**Last Updated:** December 7, 2025

## 1. Data Collection
TruthLens ("the Extension") is designed with privacy as a core principle.
*   **No Personal Data**: We do not collect, store, or transmit your personal information, browsing history, or cookies.
*   **On-Demand Processing**: The Extension only processes text that you explicitly select and choose to verify. It does not passively monitor your browsing activity.

## 2. Data Usage
When you use the "Verify" feature:
1.  The selected text is sent to your **local backend server** (running on your machine or your own hosted infrastructure).
2.  Your backend server transmits the text to the **Google Gemini API** for analysis.
3.  The analysis results are sent back to the Extension for display.

## 3. Third-Party Services
*   **Google Gemini API**: The Extension relies on the Google Gemini API for text analysis and fact-checking. Please refer to [Google's Privacy Policy](https://policies.google.com/privacy) for information on how they handle data.
*   **Local Server**: Since the backend server is self-hosted by you, you retain full control over the API keys and server logs.

## 4. Permissions
The Extension requires the following permissions to function:
*   `activeTab`: To access the selected text on the current page when you trigger the verification.
*   `contextMenus`: To add the "Verify with Sources" option to the right-click menu.
*   `host_permissions` (`http://localhost:3000/*`): To communicate with your local backend server.

## 5. Contact
If you have any questions about this Privacy Policy, please contact the developer via the support link on the Chrome Web Store.
