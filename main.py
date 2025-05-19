from router import OpenRouter

if __name__ == "__main__":
    router = OpenRouter()

    # Code review example (assumes path to code is provided)
    # code_review_result = router.route("code_review", "./path/to/your/code")
    # print("Code Review Result:\n", code_review_result)

    # Design review example (assumes a design description string is provided)
    pdf_path = "./documents/COPPER-Design Review_ Installation App Token exchange-190525-170327.pdf"
    design_review_result = router.route("design_review", pdf_path)
    print("Design Review Result:\n", design_review_result)