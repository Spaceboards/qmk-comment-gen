def repl(kmap):
    #BASIC KEYCODES
    kmap=kmap.replace("KC_NO,"," Null ,")
    kmap=kmap.replace("XXXXXXX,"," Null ,")
    kmap=kmap.replace("_______,","      ,")
    kmap=kmap.replace("KC_TRNS,","      ,")
    kmap=kmap.replace("KC_A,","   A  ,")
    kmap=kmap.replace("KC_B,","   B  ,")
    kmap=kmap.replace("KC_C,","   C  ,")
    kmap=kmap.replace("KC_D,","   D  ,")
    kmap=kmap.replace("KC_E,","   E  ,")
    kmap=kmap.replace("KC_F,","   F  ,")
    kmap=kmap.replace("KC_G,","   G  ,")
    kmap=kmap.replace("KC_H,","   H  ,")
    kmap=kmap.replace("KC_I,","   I  ,")
    kmap=kmap.replace("KC_J,","   J  ,")
    kmap=kmap.replace("KC_K,","   K  ,")
    kmap=kmap.replace("KC_L,","   L  ,")
    kmap=kmap.replace("KC_M,","   M  ,")
    kmap=kmap.replace("KC_N,","   N  ,")
    kmap=kmap.replace("KC_O,","   O  ,")
    kmap=kmap.replace("KC_P,","   P  ,")
    kmap=kmap.replace("KC_Q,","   Q  ,")
    kmap=kmap.replace("KC_R,","   R  ,")
    kmap=kmap.replace("KC_S,","   S  ,")
    kmap=kmap.replace("KC_T,","   T  ,")
    kmap=kmap.replace("KC_U,","   U  ,")
    kmap=kmap.replace("KC_V,","   V  ,")
    kmap=kmap.replace("KC_W,","   W  ,")
    kmap=kmap.replace("KC_X,","   X  ,")
    kmap=kmap.replace("KC_Y,","   Y  ,")
    kmap=kmap.replace("KC_Z,","   Z  ,")
    kmap=kmap.replace("KC_1,","   1  ,")
    kmap=kmap.replace("KC_2,","   2  ,")
    kmap=kmap.replace("KC_3,","   3  ,")
    kmap=kmap.replace("KC_4,","   4  ,")
    kmap=kmap.replace("KC_5,","   5  ,")
    kmap=kmap.replace("KC_6,","   6  ,")
    kmap=kmap.replace("KC_7,","   7  ,")
    kmap=kmap.replace("KC_8,","   8  ,")
    kmap=kmap.replace("KC_9,","   9  ,")
    kmap=kmap.replace("KC_0,","   0  ,")
    kmap=kmap.replace("KC_ENTER,","Enter ,")
    kmap=kmap.replace("KC_ENT,","Enter ,")
    kmap=kmap.replace("KC_ESC,"," Esc  ,")
    kmap=kmap.replace("KC_ESCAPE,"," Esc  ,")
    kmap=kmap.replace("KC_BSPACE,"," Bksp ,")
    kmap=kmap.replace("KC_BSPC,"," Bksp ,")
    kmap=kmap.replace("KC_TAB,"," Tab  ,")
    kmap=kmap.replace("KC_SPACE,","Space ,")
    kmap=kmap.replace("KC_SPC,","Space ,")
    kmap=kmap.replace("KC_MINUS,","  -   ,")
    kmap=kmap.replace("KC_MINS,","  -   ,")
    kmap=kmap.replace("KC_LBRACKET,","  [   ,")
    kmap=kmap.replace("KC_LBRC,","  [   ,")
    kmap=kmap.replace("KC_RBRACKET,","  ]   ,")
    kmap=kmap.replace("KC_RBRC,","  ]   ,")
    kmap=kmap.replace("KC_BSLASH,","  \   ,")
    kmap=kmap.replace("KC_BSLS,","  \   ,")
    kmap=kmap.replace("KC_NONUS_HASH,","   #  ,")
    kmap=kmap.replace("KC_NUHS,","   #  ,")
    kmap=kmap.replace("KC_SCOLON,","   ;  ,")
    kmap=kmap.replace("KC_SCLN,","   ;  ,")
    kmap=kmap.replace("KC_QUOTE,","  '   ,")
    kmap=kmap.replace("KC_QUOT,","   '  ,")
    kmap=kmap.replace("KC_GRAVE,"," `   ,")
    kmap=kmap.replace("KC_GRV,","   `  ,")
    kmap=kmap.replace("KC_COMMA,","  REPLACE,   ,")
    kmap=kmap.replace("KC_COMM,","   REPLACE,  ,")
    kmap=kmap.replace("KC_DOT,","   .  ,")
    kmap=kmap.replace("KC_SLASH,","  /   ,")
    kmap=kmap.replace("KC_SLSH,","   /  ,")
    kmap=kmap.replace("KC_CAPSLOCK,"," Caps ,")
    kmap=kmap.replace("KC_CLCK,"," Caps ,")
    kmap=kmap.replace("KC_CAPS,"," Caps ,")
    kmap=kmap.replace("KC_F1,","  F1  ,")
    kmap=kmap.replace("KC_F2,","  F2  ,")
    kmap=kmap.replace("KC_F3,","  F3  ,")
    kmap=kmap.replace("KC_F4,","  F4  ,")
    kmap=kmap.replace("KC_F5,","  F5  ,")
    kmap=kmap.replace("KC_F6,","  F6  ,")
    kmap=kmap.replace("KC_F7,","  F7  ,")
    kmap=kmap.replace("KC_F8,","  F8  ,")
    kmap=kmap.replace("KC_F9,","  F9  ,")
    kmap=kmap.replace("KC_F10,","  F10 ,")
    kmap=kmap.replace("KC_F11,","  F11 ,")
    kmap=kmap.replace("KC_F12,","  F12 ,")
    kmap=kmap.replace("KC_PSCREEN,","PrtScn,")
    kmap=kmap.replace("KC_PSCR,","PrtScn,")
    kmap=kmap.replace("KC_SCROLLLOCK,"," SclLk,")
    kmap=kmap.replace("KC_SLCK,"," ScrLk,")
    kmap=kmap.replace("KC_PAUSE,"," Paus ,")
    kmap=kmap.replace("KC_PAUS,"," Paus ,")
    kmap=kmap.replace("KC_BRK,","  Break,")
    kmap=kmap.replace("KC_INSERT,"," Break,")
    kmap=kmap.replace("KC_INS,","  Ins ,")
    kmap=kmap.replace("KC_HOME,"," Home ,")
    kmap=kmap.replace("KC_PGUP,"," PgUp ,")
    kmap=kmap.replace("KC_DELETE,","  Del ,")
    kmap=kmap.replace("KC_DEL,","  Del ,")
    kmap=kmap.replace("KC_END,","  End ,")
    kmap=kmap.replace("KC_PGDOWN,"," PgUp ,")
    kmap=kmap.replace("KC_RIGHT,"," Right,")
    kmap=kmap.replace("KC_RGHT,"," Right,")
    kmap=kmap.replace("KC_LEFT,"," Left ,")
    kmap=kmap.replace("KC_UP,"," Left ,")
    kmap=kmap.replace("KC_NUMLOCK,"," # Lk ,")
    kmap=kmap.replace("KC_NLCK,"," # Lk ,")
    kmap=kmap.replace("KC_KP_SLASH,","  /   ,")
    kmap=kmap.replace("KC_PSLS,","   /  ,")
    kmap=kmap.replace("KC_KP_ASTERISK,","   *  ,")
    kmap=kmap.replace("KC_PAST,","   *  ,")
    kmap=kmap.replace("KC_KP_MINUS,","  -   ,")
    kmap=kmap.replace("KC_PMNS,","  -   ,")
    kmap=kmap.replace("KC_KP_PLUS,","   +  ,")
    kmap=kmap.replace("KC_PPLS,","   +  ,")
    kmap=kmap.replace("KC_KP_ENTER,"," Entr ,")
    kmap=kmap.replace("KC_PENT,"," Entr ,")
    kmap=kmap.replace("KC_KP_1,","  1   ,")
    kmap=kmap.replace("KC_P1,","  1   ,")
    kmap=kmap.replace("KC_KP_2,","  2   ,")
    kmap=kmap.replace("KC_P2,","  2   ,")
    kmap=kmap.replace("KC_KP_3,","  3   ,")
    kmap=kmap.replace("KC_P3,","  3   ,")
    kmap=kmap.replace("KC_KP_4,","  4   ,")
    kmap=kmap.replace("KC_P4,","  4   ,")
    kmap=kmap.replace("KC_KP_5,","  5   ,")
    kmap=kmap.replace("KC_P5,","  5   ,")
    kmap=kmap.replace("KC_KP_6,","  6   ,")
    kmap=kmap.replace("KC_P6,","  6   ,")
    kmap=kmap.replace("KC_KP_7,","  7   ,")
    kmap=kmap.replace("KC_P7,","  7   ,")
    kmap=kmap.replace("KC_KP_8,","  8   ,")
    kmap=kmap.replace("KC_P8,","  8   ,")
    kmap=kmap.replace("KC_KP_9,","  9   ,")
    kmap=kmap.replace("KC_P9,","  9   ,")
    kmap=kmap.replace("KC_KP_0,","  0   ,")
    kmap=kmap.replace("KC_P0,","  0   ,")
    kmap=kmap.replace("KC_KP_DOT,","   .  ,")
    kmap=kmap.replace("KC_PDOT,","   .  ,")
    kmap=kmap.replace("KC_NONUS_BSLASH,","  \   ,")
    kmap=kmap.replace("KC_NUBS,","  \   ,")
    kmap=kmap.replace("KC_APPLICATION,"," App  ,")
    kmap=kmap.replace("KC_APP,"," App  ,")
    kmap=kmap.replace("KC_POWER,"," Pwr  ,")
    kmap=kmap.replace("KC_KP_EQUAL,","  =   ,")
    kmap=kmap.replace("KC_PEQL,","  =   ,")
    kmap=kmap.replace("KC_F13,","  F13 ,")
    kmap=kmap.replace("KC_F14,","  F14 ,")
    kmap=kmap.replace("KC_F15,","  F15 ,")
    kmap=kmap.replace("KC_F16,","  F16 ,")
    kmap=kmap.replace("KC_F17,","  F17 ,")
    kmap=kmap.replace("KC_F18,","  F18 ,")
    kmap=kmap.replace("KC_F19,","  F19 ,")
    kmap=kmap.replace("KC_F20,","  F20 ,")
    kmap=kmap.replace("KC_F21,","  F21 ,")
    kmap=kmap.replace("KC_F22,","  F22 ,")
    kmap=kmap.replace("KC_F23,","  F23 ,")
    kmap=kmap.replace("KC_F24,","  F24 ,")
    kmap=kmap.replace("KC_EXECUTE,"," Exec ,")
    kmap=kmap.replace("KC_EXEC,"," Exec ,")
    kmap=kmap.replace("KC_HELP,"," Help ,")
    kmap=kmap.replace("KC_MENU,"," Menu ,")
    kmap=kmap.replace("KC_SELECT,"," Slct ,")
    kmap=kmap.replace("KC_SLCT,"," Slct ,")
    kmap=kmap.replace("KC_STOP,"," Stop ,")
    kmap=kmap.replace("KC_AGAIN,","  Again,")
    kmap=kmap.replace("KC_AGIN,","  Again,")
    kmap=kmap.replace("KC_UNDO,"," Undo ,")
    kmap=kmap.replace("KC_CUT,","  Cut ,")
    kmap=kmap.replace("KC_COPY,"," Copy ,")
    kmap=kmap.replace("KC_PASTE,"," Paste,")
    kmap=kmap.replace("KC_PSTE,"," Paste,")
    kmap=kmap.replace("KC_FIND,"," Find ,")
    kmap=kmap.replace("KC__MUTE,"," Mute ,")
    kmap=kmap.replace("KC__VOLUP,"," Vol+ ,")
    kmap=kmap.replace("KC__VOLDOWN,"," Vol- ,")
    kmap=kmap.replace("KC_LOCKING_CAPS,"," Caps ,")
    kmap=kmap.replace("KC_LCAP,"," Caps ,")
    kmap=kmap.replace("KC_LOCKING_NUM,"," # Lk ,")
    kmap=kmap.replace("KC_LNUM,"," # Lk ,")
    kmap=kmap.replace("KC_LOCKING_SCROLL,"," LkScr,")
    kmap=kmap.replace("KC_LSCR,"," LkScr,")
    kmap=kmap.replace("KC_KP_COMMA,","   REPLACE,  ,")
    kmap=kmap.replace("KC_PCMM,","   REPLACE,  ,")
    kmap=kmap.replace("KC_KP_EQUAL_AS400,","  =   ,")
    kmap=kmap.replace("KC_INT1,","  \   ,")
    kmap=kmap.replace("KC_RO,","   \  ,")
    kmap=kmap.replace("KC_INT2,"," Kata ,")
    kmap=kmap.replace("KC_KANA,"," Kata ,")
    kmap=kmap.replace("KC_INT3,","  ¥   ,")
    kmap=kmap.replace("KC_JYEN,","  ¥   ,")
    kmap=kmap.replace("KC_INT4,"," Henk ,")
    kmap=kmap.replace("KC_HENK,"," Henk ,")
    kmap=kmap.replace("KC_INT5,"," Muhn ,")
    kmap=kmap.replace("KC_MHEN,"," Muhn ,")
    kmap=kmap.replace("KC_INT6,","  ,   ,")
    kmap=kmap.replace("KC_INT7,"," Int7 ,")
    kmap=kmap.replace("KC_INT8,"," Int8 ,")
    kmap=kmap.replace("KC_INT9,"," Int9 ,")
    kmap=kmap.replace("KC_LANG1,"," En/Ha,")
    kmap=kmap.replace("KC_HAEN,"," En/Ha,")
    kmap=kmap.replace("KC_LANG2,"," Hanja,")
    kmap=kmap.replace("KC_HANJ,"," Hanja,")
    kmap=kmap.replace("KC_LANG3,"," Kata ,")
    kmap=kmap.replace("KC_LANG4,"," Hira ,")
    kmap=kmap.replace("KC_LANG5,"," Zenk ,")
    kmap=kmap.replace("KC_LANG6,"," Lang6,")
    kmap=kmap.replace("KC_LANG7,"," Lang7,")
    kmap=kmap.replace("KC_LANG8,"," Lang8,")
    kmap=kmap.replace("KC_LANG9,"," Lang9,")
    kmap=kmap.replace("KC_ALT_ERASE,"," Erase,")
    kmap=kmap.replace("KC_ERAS,"," Erase,")
    kmap=kmap.replace("KC_SYSREQ,"," Attn ,")
    kmap=kmap.replace("KC_CANCEL,"," Cncl ,")
    kmap=kmap.replace("KC_CLEAR,"," Clr  ,")
    kmap=kmap.replace("KC_CLR,"," Clr  ,")
    kmap=kmap.replace("KC_PRIOR,"," Prior,")
    kmap=kmap.replace("KC_RETURN,"," Rtrn ,")
    kmap=kmap.replace("KC_SEPARATOR,","  Sep ,")
    kmap=kmap.replace("KC_OUT,","  Out ,")
    kmap=kmap.replace("KC_OPER,"," Oper ,")
    kmap=kmap.replace("KC_CLEAR_AGAIN,"," ClAg ,")
    kmap=kmap.replace("KC_EXSEL,"," ExSel,")
    kmap=kmap.replace("KC_LCTRL,"," Ctrl ,")
    kmap=kmap.replace("KC_LCTL,"," Ctrl ,")
    kmap=kmap.replace("KC_LSHIFT,"," Shft ,")
    kmap=kmap.replace("KC_LSFT,"," Shft ,")
    kmap=kmap.replace("KC_LALT,"," Alt  ,")
    kmap=kmap.replace("KC_LGUI,"," Gui  ,")
    kmap=kmap.replace("KC_LCMD,"," Cmd  ,")
    kmap=kmap.replace("KC_LWIN,"," Win  ,")
    kmap=kmap.replace("KC_RCTRL,"," Ctrl ,")
    kmap=kmap.replace("KC_RCTL,"," Ctrl ,")
    kmap=kmap.replace("KC_RSHIFT,"," Shft ,")
    kmap=kmap.replace("KC_RSFT,"," Shft ,")
    kmap=kmap.replace("KC_RALT,"," Alt  ,")
    kmap=kmap.replace("KC_ALGR,"," Alt  ,")
    kmap=kmap.replace("KC_RGUI,"," Gui  ,")
    kmap=kmap.replace("KC_RCMD,"," Cmd  ,")
    kmap=kmap.replace("KC_RWIN,"," Win  ,")
    kmap=kmap.replace("KC_SYSTEM_POWER,"," Pwr  ,")
    kmap=kmap.replace("KC_PWR,"," Pwr  ,")
    kmap=kmap.replace("KC_SYSTEM_SLEEP,"," Sleep,")
    kmap=kmap.replace("KC_SLEP,"," Sleep,")
    kmap=kmap.replace("KC_SYSTEM_WAKE,"," Wake ,")
    kmap=kmap.replace("KC_WAKE,"," Wake ,")
    kmap=kmap.replace("KC_AUDIO_MUTE,"," Mute ,")
    kmap=kmap.replace("KC_MUTE,"," Mute ,")
    kmap=kmap.replace("KC_AUDIO_VOL_UP,"," Vol+ ,")
    kmap=kmap.replace("KC_VOLU,"," Vol+ ,")
    kmap=kmap.replace("KC_AUDIO_VOL_DOWN,"," Vol- ,")
    kmap=kmap.replace("KC_VOLD,"," Vol- ,")
    kmap=kmap.replace("KC_MEDIA_NEXT_TRACK,"," Next ,")
    kmap=kmap.replace("KC_MNXT,"," Next ,")
    kmap=kmap.replace("KC_MEDIA_PREV_TRACK,"," Prev ,")
    kmap=kmap.replace("KC_MPRV,"," Prev ,")
    kmap=kmap.replace("KC_MEDIA_STOP,"," Stop ,")
    kmap=kmap.replace("KC_MSTP,"," Stop ,")
    kmap=kmap.replace("KC_MEDIA_PLAY_PAUSE,"," Play ,")
    kmap=kmap.replace("KC_MPLY,"," Play ,")
    kmap=kmap.replace("KC_MEDIA_SELECT,"," Slct ,")
    kmap=kmap.replace("KC_MSEL,"," Slct ,")
    kmap=kmap.replace("KC_MEDIA_EJECT,"," Ejct ,")
    kmap=kmap.replace("KC_EJCT,"," Ejct ,")
    kmap=kmap.replace("KC_MAIL,"," Mail ,")
    kmap=kmap.replace("KC_CALCULATOR,"," Calc ,")
    kmap=kmap.replace("KC_CALC,"," Calc ,")
    kmap=kmap.replace("KC_MY_COMPUTER,"," MyPC ,")
    kmap=kmap.replace("KC_MYCM,"," MyPC ,")
    kmap=kmap.replace("KC_WWW_SEARCH,"," Srch ,")
    kmap=kmap.replace("KC_WSCH,"," Srch ,")
    kmap=kmap.replace("KC_WWW_HOME,"," Home ,")
    kmap=kmap.replace("KC_WHOM,"," Home ,")
    kmap=kmap.replace("KC_WWW_BACK,"," Back ,")
    kmap=kmap.replace("KC_WBAK,"," Back ,")
    kmap=kmap.replace("KC_WWW_FORWARD,"," Frwd ,")
    kmap=kmap.replace("KC_WFWD,"," Frwd ,")
    kmap=kmap.replace("KC_WWW_STOP,"," Stop ,")
    kmap=kmap.replace("KC_WSTOP,"," Stop ,")
    kmap=kmap.replace("KC_WWW_REFRESH,"," Rfsh ,")
    kmap=kmap.replace("KC_WREF,"," Rfsh ,")
    kmap=kmap.replace("KC_WWW_FAVORITES,"," Fav  ,")
    kmap=kmap.replace("KC_WFAV,"," Fav  ,")
    kmap=kmap.replace("KC_MEDIA_FAST_FORWARD,","  >>  ,")
    kmap=kmap.replace("KC_MFFD,","  >>  ,")
    kmap=kmap.replace("KC_MEDIA_REWIND,","  <<  ,")
    kmap=kmap.replace("KC_MRWD,","  <<  ,")
    kmap=kmap.replace("KC_BRIGHTNESS_UP,"," Brt+ ,")
    kmap=kmap.replace("KC_BRIU,"," Brt+ ,")
    kmap=kmap.replace("KC_BRIGHTNESS_DOWN,"," Brt- ,)
    kmap=kmap.replace("KC_BRID,"," Brt- ,")
    #QUANTUM KEYCODES
    kmap=kmap.replace("RESET,"," Reset,")
    kmap=kmap.replace("DEBUG,"," Debug,")
    kmap=kmap.replace("EEPROM_RESET,","EepRst,")
    kmap=kmap.replace("EEP_RST,","EepRst,")
    kmap=kmap.replace("KC_GESC,"," `/Esc,")
    kmap=kmap.replace("GRAVE_ESC,"," `/Esc,")
    kmap=kmap.replace("KC_LSPO,"," Shf/(,")
    kmap=kmap.replace("KC_RSPC,"," Shf/),")
    kmap=kmap.replace("KC_LEAD,"," Lead ,")
    kmap=kmap.replace("KC_LOCK,"," Lock ,")
    #cant do these rn (M, MACROTAP)
    #AUDIO KEYS
    kmap=kmap.replace("AU_ON,","Au On ,")
    kmap=kmap.replace("AU_OFF,","Au Off,")
    kmap=kmap.replace("AU_TOG,","Au Tog,")
    kmap=kmap.replace("CLICKY_TOGGLE,","Ck Tog,")
    kmap=kmap.replace("CK_TOGG,","Ck Tog,")
    kmap=kmap.replace("CLICKY_UP,"," Ck Up,")
    kmap=kmap.replace("CK_UP,"," Ck Up,")
    kmap=kmap.replace("CLICKY_RESET,","Ck Rst,")
    kmap=kmap.replace("CK_RST,","Ck Rst,")
    kmap=kmap.replace("MU_ON,","Mu On ,")
    kmap=kmap.replace("MU_OFF,","Mu Off,")
    kmap=kmap.replace("MU_TOG,","Mu Tog,")
    kmap=kmap.replace("MU_MOD,","Mu Mod,")
    #BACKLIGHTING
    kmap=kmap.replace("BL_TOGG,","BL Tog,")
    kmap=kmap.replace("BL_STEP,","BL Stp,")
    kmap=kmap.replace("BL_ON,","BL On ,")
    kmap=kmap.replace("BL_OFF,","BL Off,")
    kmap=kmap.replace("BL_INC,"," BL + ,")
    kmap=kmap.replace("BL_DEC,"," BL - ,")
    kmap=kmap.replace("BL_BRTG,","BL Brt,")
    #BOOTMAGIC NOT SUPPORTED
    #BLUETOOTH
    kmap=kmap.replace("OUT_AUTO,"," Auto ,")
    kmap=kmap.replace("OUT_USB,"," F USB,")
    kmap=kmap.replace("OUT_BT,"," F BT ,")
    #LAYER SWITCHING NOT SUPPORTED
    #MOUSE KEYS
    kmap=kmap.replace("KC_MS_UP,","MS Up ,")
    kmap=kmap.replace("KC_MS_U,","MS Up ,")
    kmap=kmap.replace("KC_MS_DOWN,","MS Dw ,")
    kmap=kmap.replace("KC_MS_D,","MS Dw ,")
    kmap=kmap.replace("KC_MS_LEFT,","MS Lft")
    kmap=kmap.replace("KC_MS_L,","MS Lf ,")
    kmap=kmap.replace("KC_MS_RIGHT,","MS Rgt,")
    kmap=kmap.replace("KC_MS_R,","MS Rgt,")
    kmap=kmap.replace("KC_MS_BTN1,"," MS B1,")
    kmap=kmap.replace("KC_BTN1,"," MS B1,")
    kmap=kmap.replace("KC_MS_BTN2,"," MS B2,")
    kmap=kmap.replace("KC_BTN2,"," MS B2,")
    kmap=kmap.replace("KC_MS_BTN3,"," MS B3,")
    kmap=kmap.replace("KC_BTN3,"," MS B3,")
    kmap=kmap.replace("KC_MS_BTN4,"," Ms B4,")
    kmap=kmap.replace("KC_BTN4,"," MS B4,")
    kmap=kmap.replace("KC_MS_BTN5,"," MS B5,")
    kmap=kmap.replace("KC_BTN5,"," MS B5,")
    kmap=kmap.replace("KC_MS_WH_UP,"," WH Up,")
    kmap=kmap.replace("KC_WH_U,"," WH Up,")
    kmap=kmap.replace("KC_MS_WH_DOWN,"," WH Dw,")
    kmap=kmap.replace("KC_WH_D,"," WH Dw,")
    kmap=kmap.replace("KC_MS_WH_LEFT,","WH Lft,")
    kmap=kmap.replace("KC_WH_L,","WH Lft,")
    kmap=kmap.replace("KC_MS_WH_RIGHT,","WH Rgt,")
    kmap=kmap.replace("KC_WH_R,","WH Lft,")
    kmap=kmap.replace("KC_MS_ACCEL0,"," Acl 0,")
    kmap=kmap.replace("KC_ACL0,"," Acl 0,")    
    kmap=kmap.replace("KC_MS_ACCEL1,"," Acl 1,")
    kmap=kmap.replace("KC_ACL1,"," Acl 1,")
    kmap=kmap.replace("KC_MS_ACCEL2,"," Acl 2,")
    kmap=kmap.replace("KC_ACL2,"," Acl 2,")
    #MODIFIERS NOT SUPPORTED
    #MOD-TAP KEYS NOT SUPPORTED
    #US ANSI SHIFTED SYMBOLS
    kmap=kmap.replace("KC_TILDE,","  ~   ,")
    kmap=kmap.replace("KC_TILD,","  ~   ,")
    kmap=kmap.replace("KC_EXCLAIM,","  !   ,")
    kmap=kmap.replace("KC_EXLM,","  !   ,")
    kmap=kmap.replace("KC_AT,","  @   ,")
    kmap=kmap.replace("KC_HASH,","  #   ,")
    kmap=kmap.replace("KC_DOLLAR,","  $   ,")
    kmap=kmap.replace("KC_DLR,","  $   ,")
    kmap=kmap.replace("KC_PERCENT,","  %   ,")
    kmap=kmap.replace("KC_PERC,","  %   ,")
    kmap=kmap.replace("KC_CIRCUMFLEX,","  ^   ,")
    kmap=kmap.replace("KC_CIRC,","  ^   ,")
    kmap=kmap.replace("KC_AMPERSAND,","  &   ,")
    kmap=kmap.replace("KC_AMPR,","  &   ,")
    kmap=kmap.replace("KC_ASTERISK,","  *   ,")
    kmap=kmap.replace("KC_ASTR,","  *   ,")
    kmap=kmap.replace("KC_LEFT_PAREN,","  (   ,")
    kmap=kmap.replace("KC_LPRN,","  (   ,")
    kmap=kmap.replace("KC_RIGHT_PAREN,","  )   ,")
    kmap=kmap.replace("KC_RPRN,","  )   ,")
    kmap=kmap.replace("KC_UNDERSCORE,","  _   ,")
    kmap=kmap.replace("KC_UNDS,","  _   ,")
    kmap=kmap.replace("KC_PLUS,","  +   ,")
    kmap=kmap.replace("KC_LEFT_CURLY_BRACE,","  {   ,")
    kmap=kmap.replace("KC_LCBR,","  {   ,")
    kmap=kmap.replace("KC_RIGHT_CURLY_BRACE,","  }   ,")
    kmap=kmap.replace("KC_RCBR,","  }   ,")
    kmap=kmap.replace("KC_PIPE,","  |   ,")
    kmap=kmap.replace("KC_COLON,","  :   ,")
    kmap=kmap.replace("KC_COLN,","  :   ,")
    kmap=kmap.replace("KC_DOUBLE_QUOTE,","  \"   ,")
    kmap=kmap.replace("KC_DQUO,","  \"   ,")
    kmap=kmap.replace("KC_DQT,","  \"    ,")
    kmap=kmap.replace("KC_LEFT_ANGLE_BRACKET,","  <   ,")
    kmap=kmap.replace("KC_LABK,","  <   ,")
    kmap=kmap.replace("KC_LT,","  <   ,")
    kmap=kmap.replace("KC_RIGHT_ANGLE_BRACKET,","  >   ,")
    kmap=kmap.replace("KC_RABK,","  >   ,")
    kmap=kmap.replace("KC_GT,","  >   ,")
    kmap=kmap.replace("KC_QUESTION,","  ?   ,")
    kmap=kmap.replace("KC_QUES,","  ?   ,")
    #ONE SHOT KEYS NOT SUPPORTED
    #SWAP HANDS (SH_T() NOT SUPPORTED)
    kmap=kmap.replace("SW_ON,"," SW On,")
    kmap=kmap.replace("SW_OFF,","SW Off,")
    kmap=kmap.replace("SH_MON,","SH Mmt,")
    kmap=kmap.replace("SH_MOFF,","SH Mof,")
    kmap=kmap.replace("SH_TG,"," SH Tog,")
    kmap=kmap.replace("SH_TT,"," SH TgM,")
    #UNICODE NOT SUPPORTED

    kmap=kmap.replace(" ,"," |")
    kmap=kmap.replace("*,","*|")
    kmap=kmap.replace("REPLACE,",",")
    return kmap
