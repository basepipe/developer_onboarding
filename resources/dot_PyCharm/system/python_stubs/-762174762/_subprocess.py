# encoding: utf-8
# module _subprocess
# from (built-in)
# by generator 1.147
# no doc
# no imports

# Variables with simple values

CREATE_NEW_CONSOLE = 16

CREATE_NEW_PROCESS_GROUP = 512

DUPLICATE_SAME_ACCESS = 2

INFINITE = -1

STARTF_USESHOWWINDOW = 1
STARTF_USESTDHANDLES = 256

STD_ERROR_HANDLE = -12

STD_INPUT_HANDLE = -10

STD_OUTPUT_HANDLE = -11

STILL_ACTIVE = 259

SW_HIDE = 0

WAIT_OBJECT_0 = 0

# functions

def CreatePipe(pipe_attrs, size): # real signature unknown; restored from __doc__
    """
    CreatePipe(pipe_attrs, size) -> (read_handle, write_handle)
    
    Create an anonymous pipe, and return handles to the read and
    write ends of the pipe.
    
    pipe_attrs is ignored internally and can be None.
    """
    pass

def CreateProcess(app_name, cmd_line, proc_attrs, thread_attrs, inherit, flags, env_mapping, curdir, startup_info): # real signature unknown; restored from __doc__
    """
    CreateProcess(app_name, cmd_line, proc_attrs, thread_attrs,
                   inherit, flags, env_mapping, curdir,
                   startup_info) -> (proc_handle, thread_handle,
                                     pid, tid)
    
    Create a new process and its primary thread. The return
    value is a tuple of the process handle, thread handle,
    process ID, and thread ID.
    
    proc_attrs and thread_attrs are ignored internally and can be None.
    """
    pass

def DuplicateHandle(source_proc_handle, source_handle, target_proc_handle, target_handle, access, inherit, options=None): # real signature unknown; restored from __doc__
    """
    DuplicateHandle(source_proc_handle, source_handle,
                     target_proc_handle, target_handle, access,
                     inherit[, options]) -> handle
    
    Return a duplicate handle object.
    
    The duplicate handle refers to the same object as the original
    handle. Therefore, any changes to the object are reflected
    through both handles.
    """
    pass

def GetCurrentProcess(): # real signature unknown; restored from __doc__
    """
    GetCurrentProcess() -> handle
    
    Return a handle object for the current process.
    """
    pass

def GetExitCodeProcess(handle): # real signature unknown; restored from __doc__
    """
    GetExitCodeProcess(handle) -> Exit code
    
    Return the termination status of the specified process.
    """
    pass

def GetModuleFileName(module): # real signature unknown; restored from __doc__
    """
    GetModuleFileName(module) -> path
    
    Return the fully-qualified path for the file that contains
    the specified module. The module must have been loaded by the
    current process.
    
    The module parameter should be a handle to the loaded module
    whose path is being requested. If this parameter is 0, 
    GetModuleFileName retrieves the path of the executable file
    of the current process.
    """
    pass

def GetStdHandle(handle): # real signature unknown; restored from __doc__
    """
    GetStdHandle(handle) -> integer
    
    Return a handle to the specified standard device
    (STD_INPUT_HANDLE, STD_OUTPUT_HANDLE, STD_ERROR_HANDLE).
    The integer associated with the handle object is returned.
    """
    return 0

def GetVersion(): # real signature unknown; restored from __doc__
    """
    GetVersion() -> version
    
    Return the version number of the current operating system.
    """
    pass

def TerminateProcess(handle, exit_code): # real signature unknown; restored from __doc__
    """
    TerminateProcess(handle, exit_code) -> None
    
    Terminate the specified process and all of its threads.
    """
    pass

def WaitForSingleObject(handle, timeout): # real signature unknown; restored from __doc__
    """
    WaitForSingleObject(handle, timeout) -> result
    
    Wait until the specified object is in the signaled state or
    the time-out interval elapses. The timeout value is specified
    in milliseconds.
    """
    pass

# no classes
