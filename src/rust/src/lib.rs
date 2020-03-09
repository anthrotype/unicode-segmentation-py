extern crate unicode_segmentation;

use std::ffi::CStr;
use std::os::raw::c_char;
use std::os::raw::c_ulong;
use unicode_segmentation::UnicodeSegmentation;

#[no_mangle]
pub unsafe extern "C" fn graphemes(
    s: *const c_char,
    output: *mut c_ulong,
    output_size: *mut c_ulong,
) -> bool {
    assert!(!s.is_null(), "input string is NULL");
    assert!(!output.is_null(), "output array is NULL");

    let rs = CStr::from_ptr(s)
        .to_str()
        .expect("input must be valid UTF8");
    let graphemes = UnicodeSegmentation::grapheme_indices(rs, true).collect::<Vec<(usize, &str)>>();
    let indices: Vec<usize> = graphemes.iter().map(|e| e.0).collect();
    // println!("{:?}", indices);

    let output_slice = std::slice::from_raw_parts_mut(output as *mut u64, indices.len());
    for (i, v) in indices.iter().enumerate() {
        output_slice[i] = *v as u64;
    }
    *output_size = indices.len() as u64;

    true
}
