# 원클릭 설치 프롬프트

아래 전체를 로컬 파일과 터미널 권한이 있는 Claude Code 또는 Codex에 복사하세요.

[中文](one-click-import.md) · **한국어**

```text
https://github.com/XiaoyeCodes/code-animation-prompts 를 현재 코딩 어시스턴트에서 사용할 수 있는 skill로 설치해 주세요.

1. 저장소를 적절한 로컬 디렉터리에 다운로드하세요. 같은 이름의 디렉터리가 이미 있으면 먼저 내용을 확인하고, 기존 변경 사항을 덮어쓰지 마세요.
2. README.ko.md, docs/INSTALL.ko.md, skills/code-animation-prompts/SKILL.md를 읽으세요.
3. 현재 어시스턴트에 맞는 설치 대상을 선택하세요. Codex는 ~/.agents/skills/code-animation-prompts,
   Claude Code는 ~/.claude/skills/code-animation-prompts를 사용합니다.
   저장소 루트에서 python scripts/install_skill.py --target codex 또는 --target claude를 실행하세요.
   현재 어시스턴트를 판별할 수 없으면 대상만 저에게 확인하고, 두 위치에 임의로 설치하지 마세요.
4. 설치할 때 assets/library 안의 모든 프롬프트, 스틸, HTML, 예시 영상, 라이선스 파일을 포함한
   전체 skill 폴더를 유지하세요. 대상이 이미 존재하면 기존 디렉터리를 보존하고 보고하며,
   자동으로 삭제하거나 덮어쓰지 마세요.
5. 설치된 디렉터리에서 `scripts/styles.py search 水墨` 명령으로 스타일을 찾을 수 있는지 확인하고,
   이어서 `scripts/styles.py show B3` 명령으로 전체 프롬프트를 읽을 수 있는지 확인하세요.
6. 실제 설치 경로, 호출 방법, 새 세션이 필요한지를 알려 주세요.
   마지막으로 바로 사용할 수 있는 "12초 입자 응집 애니메이션" 요청 예시를 한 문장으로 주세요.

이번에는 스타일 skill만 설치하고, 영상 렌더링 의존성은 자동 설치하지 말고, 다른 어시스턴트 설정도 변경하지 마세요.
```

[README로 돌아가기](../README.ko.md)
