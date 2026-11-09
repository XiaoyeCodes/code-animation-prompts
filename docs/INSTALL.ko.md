# Claude Code / Codex에 설치하기

이 저장소는 로컬 파일과 터미널을 사용할 수 있는 Claude Code와 Codex를 대상으로 합니다. 먼저 전체 저장소를 다운로드하세요(원본 영상 약 75 MiB와 README 이미지 포함). 설치 대상은 `skills/code-animation-prompts/` 디렉터리 전체입니다.

[中文](INSTALL.md) · **한국어**

## 어시스턴트에게 한 문장으로 맡기기

[원클릭 설치 프롬프트 복사](../prompts/one-click-import.ko.md). 어시스턴트가 저장소를 다운로드하고, 설명을 읽고, 현재 도구에 맞는 설치 위치를 선택한 뒤 스타일 조회를 검증합니다.

## Python 설치 스크립트

Python 3.10+가 필요하며 서드파티 패키지에 의존하지 않습니다. 저장소 루트에서 실행하세요:

```bash
python scripts/install_skill.py --target codex
python scripts/install_skill.py --target claude
```

둘 중 하나만 선택하면 됩니다. `--target both`는 두 위치에 모두 설치합니다. `--dry-run`은 파일을 쓰지 않고 경로만 표시합니다.

| 도구 | 사용자 단위 디렉터리 | 프로젝트 단위 디렉터리 |
|---|---|---|
| Codex | `~/.agents/skills/code-animation-prompts/` | `<프로젝트>/.agents/skills/code-animation-prompts/` |
| Claude Code | `~/.claude/skills/code-animation-prompts/` | `<프로젝트>/.claude/skills/code-animation-prompts/` |

`~`는 사용자 홈 디렉터리를 뜻하며, Windows에서는 보통 `C:\Users\사용자이름`입니다. 경로는 [OpenAI 공식 스킬 문서](https://learn.chatgpt.com/docs/build-skills)와 [Claude Code 공식 스킬 문서](https://code.claude.com/docs/en/skills)를 기준으로 정리했습니다.

특정 프로젝트에 설치하려면:

```bash
python scripts/install_skill.py --target codex --scope project --project-dir "프로젝트 경로"
python scripts/install_skill.py --target claude --scope project --project-dir "프로젝트 경로"
```

같은 어시스턴트의 사용자 단위와 프로젝트 단위에 같은 이름의 스킬을 중복 설치하지 마세요. 동일한 이름의 진입점이 여러 개 생길 수 있습니다.

## Python을 사용하지 않을 때

저장소의 `skills/code-animation-prompts/` 디렉터리 전체를 위 표의 위치로 수동 복사하세요. 최종적으로 다음 파일이 있어야 합니다:

```text
<설치 위치>/code-animation-prompts/SKILL.md
<설치 위치>/code-animation-prompts/assets/library/风格挑选.html
<설치 위치>/code-animation-prompts/references/catalog.json
```

`SKILL.md`만 복사하면 스타일 라이브러리가 빠집니다. `assets/library/` 내부 파일들의 상대 위치를 바꾸지 마세요.

## 설치 확인

`<스킬 디렉터리>`를 실제 설치 경로로 바꿔 실행하세요:

```bash
python "<스킬 디렉터리>/scripts/styles.py" search 水墨
python "<스킬 디렉터리>/scripts/styles.py" show B3
```

새 세션을 시작한 뒤 Codex에서는 `$code-animation-prompts`, Claude Code에서는 `/code-animation-prompts`를 입력합니다. "code-animation-prompts를 사용해서 애니메이션을 만들어 줘"라고 직접 말해도 됩니다. 현재 세션에 새 스킬이 보이지 않으면 세션을 다시 시작하세요. 계정 또는 관리자 설정에 따라 스킬 검색이 영향을 받을 수 있습니다.

## 업데이트

설치 스크립트는 기존 디렉터리를 덮어쓰지 않습니다. 업데이트 전에 직접 수정한 내용을 저장하고, 이전 스킬 디렉터리를 스킬 검색 디렉터리 밖으로 백업하세요. 그다음 저장소를 다시 받아 설치 명령을 다시 실행합니다. `SKILL.md`가 들어 있는 백업을 `.agents/skills/` 또는 `.claude/skills/` 아래에 남겨 두지 마세요. 계속 검색될 수 있습니다.

저장소의 소재 색인을 갱신하고 무결성을 확인하려면:

```bash
python scripts/build_catalog.py
python scripts/validate_repo.py
```

## 선택 사항: 영상 내보내기

스킬을 설치해도 브라우저나 FFmpeg가 자동으로 설치되지는 않습니다. 실제로 영상을 내보낼 때 [렌더링 안내](../skills/code-animation-prompts/references/rendering.md)에 따라 의존성을 설정하세요.

[README로 돌아가기](../README.ko.md)
