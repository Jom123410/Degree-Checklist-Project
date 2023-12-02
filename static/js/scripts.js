function toggleCourses(semester) {
    const coursesList = document.getElementById(`courses-${semester}`);
    if (coursesList.style.display === "none") {
        coursesList.style.display = "block";
    } else {
        coursesList.style.display = "none";
    }
}
