package com.shah.user_app;


import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.Optional;

@Controller
public class UserController {

    @Autowired
    private UserService userService;

    // Show the registration page
    @GetMapping("/register")
    public String showRegisterForm(HttpServletRequest request) {

        // Debugging: Log the session state and cookies
        HttpSession session = request.getSession();
        System.out.println("Session ID: " + session.getId());
        System.out.println("Is Session New? " + session.isNew());

        Object user = request.getSession().getAttribute("user"); // Example check, adjust as necessary

        // Check if the user is already logged in
        // If you have some session or user service to check login status

        if (user != null) {
            // If the user is logged in, redirect to another page (e.g., home or profile)
            return "redirect:/home";  // Redirecting logged-in users to the home page
        }
        return "register";  // Returns the register.html view
    }

    // Handle registration form submission
    @PostMapping("/register")
    public String registerUser(@RequestParam String username,
                               @RequestParam String password,
                               Model model) {
        // Check if the username already exists
        if (userService.findByUsername(username).isPresent()) {
            model.addAttribute("error", "Username already exists.");
            return "register";  // Return to the register page with an error message
        }

        // Create a new User object and set its properties
        User newUser = new User(username, password, "USER");
        userService.saveUser(newUser);  // Save the user to the database

        return "redirect:/login";  // Redirect to the login page after successful registration
    }

    // Show the login page
    @GetMapping("/login")
    public String showLoginForm() {
        return "login";  // Returns the login.html view
    }

    // Handle login form submission
    @PostMapping("/login")
    public String loginUser(@RequestParam String username,
                            @RequestParam String password,
                            Model model) {
        // Find user by username
        Optional<User> userOptional = userService.findByUsername(username);

        // Check if user exists and password matches
        if (userOptional.isPresent()) {
            User user = userOptional.get();
            if (user.getPassword().equals(password)) {
                model.addAttribute("message", "Login successful!");
                return "home";  // Redirect to the home page (or another page after successful login)
            } else {
                model.addAttribute("error", "Invalid password.");
                return "login";  // Return to the login page with an error message
            }
        } else {
            model.addAttribute("error", "Username not found.");
            return "login";  // Return to the login page with an error message
        }
    }
}


