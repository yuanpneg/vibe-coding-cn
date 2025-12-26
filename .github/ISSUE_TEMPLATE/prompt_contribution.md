---
name: "💡 贡献新的提示词 (Prompt)"
description: "分享一个您认为有价值的编程或 AI 相关的提示词。"
title: "prompt: "
labels: ["prompt", "enhancement"]
body:
  - type: markdown
    attributes:
      value: |
        非常感谢您愿意分享您的宝贵提示词！一个好的提示词能极大地提升我们的工作效率。

  - type: input
    id: prompt-name
    attributes:
      label: "提示词名称"
      description: "给您的提示词起一个简洁明了的名称。"
      placeholder: "例如：代码调试专家 (Debug Expert)"
    validations:
      required: true

  - type: textarea
    id: prompt-content
    attributes:
      label: "提示词内容"
      description: "请在此处粘贴您的完整提示词内容。请使用 Markdown 代码块进行格式化。"
      render: "markdown"
    validations:
      required: true

  - type: textarea
    id: use-case
    attributes:
      label: "使用场景和说明"
      description: "请描述这个提示词主要用于解决什么问题？它的效果如何？如果有任何使用的注意事项，也请一并说明。"
    validations:
      required: true

  - type: checkboxes
    id: checklist
    attributes:
      label: "确认清单"
      description: "在提交前，请确认以下事项。"
      options:
        - label: "我确认这个提示词是我原创或有权分享的。"
          required: true
        - label: "我已经在本地测试过这个提示词，并确认其有效性。"
          required: true
        - label: "我同意将这个提示词以项目所使用的 [MIT License](LICENSE) 授权给社区。"
          required: true