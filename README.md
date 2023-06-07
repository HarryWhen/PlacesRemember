# Places Remember

Places Remember is a Django application that integrates social authentication with VKontakte (VK) using the social_django library.

## Features

- Allows users to authenticate with their VKontakte accounts
- Retrieves the user's VKontakte profile information, including the avatar photo
- Provides a user-friendly interface for VKontakte authentication
- Supports social authentication with other providers through social_django

## Usage

1. Open the homepage and click on the "Login with VKontakte" button.
2. You will be redirected to VKontakte's authorization page. Log in with your VKontakte credentials.
3. After successful authentication, you will be redirected back to the application.
4. You can now access your VKontakte profile information, including the avatar photo, on the application's pages.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the project's GitHub repository.


## Challenges and Oversights During Development

During the development process, there were challenges encountered when working with geospatial data. As a result, I opted for lightweight solutions and maintained the bare minimum functionality.

Unfortunately, during the interface design, I overlooked the preliminary hiding of the form for data entry.

While the added map is functional, the controls may cause discomfort.

Due to time constraints, I was unable to include a badge indicating the current test coverage.

The linter is not properly configured, resulting in numerous stylistic errors. The majority of these errors point to the absence of docstrings.
